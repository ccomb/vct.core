from zope.interface import implements
from zope.component import adapts, getUtility
from vct.core.interfaces import IItem
from vct.core.db.interfaces import IDatabase
from vct.core.item import Item
import vct.core
import random

# zodb
import transaction
from BTrees.OOBTree import OOBTree
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from persistent import Persistent
from persistent.dict import PersistentDict

ZODB = DB(FileStorage('Data.fs'))

class ZodbItem(Persistent):
    """persistent item object for zodb
    """
    data = None
    uids = None
    type = None


class ItemZODBStorage(object):
    """Generic ZODB storage adapter for putting or deleting items
    """
    implements(IDatabase)
    adapts(IItem)
    def __init__(self, context):
        self.connection = ZODB.open()
        self.root = self.connection.root()
        self.context = context

    def __del__(self):
        self.connection.close()

    def put(self, uid_name=None, uid_value=None):
        zodb_item = ZodbItem()
        # if we already have an uid, retrieve the existing object
        if self.context.uids is not None and len(self.context.uids) > 0:
            first_uid_name = self.context.uids.keys()[0]
            first_uid_value = self.context.uids[first_uid_name]
            zodb_item = self.root[first_uid_name][first_uid_value]
            local_uid = zodb_item.uids[vct.core.SERVER_NAME]

        # create the given uid container
        if uid_name is not None and uid_name not in self.root:
            self.root[uid_name] = OOBTree()
        # create the implicit local_uid container
        if vct.core.SERVER_NAME not in self.root:
            self.root[vct.core.SERVER_NAME] = OOBTree()

        # if this is a new object, add it in the container
        if zodb_item.uids is None or len(zodb_item.uids) == 0:
            # store the object under a generated local uid
            local_uid = str(random.getrandbits(64))
            while local_uid in self.root[vct.core.SERVER_NAME]:
                local_uid = str(random.getrandbits(64))
            self.root[vct.core.SERVER_NAME][local_uid] = zodb_item
            if uid_name is not None and uid_value is not None:
                self.root[uid_name][uid_value] = zodb_item

        zodb_item.type = self.context.__class__.__name__.lower()
        zodb_item.data = PersistentDict(self.context.data)
        zodb_item.uids = PersistentDict(self.context.uids)
        zodb_item.uids[vct.core.SERVER_NAME] = local_uid

        # update the uids
        if uid_name is not None and uid_value is not None:
            zodb_item.uids[uid_name] = uid_value
            self.root[uid_name][uid_value] = zodb_item

        transaction.commit()
        return local_uid

    def get(self, uid=None, data=None):
        """return a tuple (number, results)
        """
        if uid is not None:
            container = self.root.get(uid[0])
            if container is None or uid[1] not in container:
                return (0, [])
            zodb_item = container[uid[1]]
            # we recreate a non persistent object
            Model = getUtility(IItem, zodb_item.type)
            item = Model()
            item.data = dict(zodb_item.data)
            item.data['type'] = zodb_item.type
            item.uids = dict(zodb_item.uids)
            # TODO item.schema?
            return (1, [item])

        if data is not None and len(data) > 0:
            # TODO awfully slow, replace with a catalog search!
            items = set()
            for container in self.root.keys():
                for zodb_item in self.root[container].values():
                    if all([key in zodb_item.data and zodb_item.data.get(key) == data.get(key) for key in data.keys()]):
                        items.add(zodb_item)
            results = []
            for i in items:
                Model = getUtility(IItem, i.type)
                item = Model()
                item.data = dict(i.data)
                item.data['type'] = i.type
                item.uids = dict(i.uids)
                results.append(item)

            return len(results), results
        return (0, [])

    def delete(self, uid_name, uid_value):
        # update the uids dict
        del self.root[uid_name][uid_value].uids[uid_name]
        # delete the reference (other may exist in other containers)
        del self.root[uid_name][uid_value]
        transaction.commit()


