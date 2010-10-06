from zope.interface import implements
from zope.component import adapts
from vct.core.interfaces import IDatabase, IItem
from vct.core.item import Item

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

class ZODBStorage(object):
    """Generic ZODB Storage utility for retrieving any objects
    """
    implements(IDatabase)
    def __init__(self):
        self.connection = ZODB.open()
        self.root = self.connection.root()

    def get(self, uid=None, data=None):
        """return a tuple (number, results)
        """
        if uid is not None:
            container = self.root.get(uid[0])
            if container is None or uid[1] not in container:
                return (0, [])
            zodb_item = container[uid[1]]
            # we recreate a non persistent object
            item = Item()
            item.data = dict(zodb_item.data)
            item.uids = dict(zodb_item.uids)
            return (1, [item])

        if data is not None:
            # TODO awfully slow, replace with a catalog search!
            results = set()
            for container in self.root.keys():
                for zodb_item in self.root[container].values():
                    if all([zodb_item.data[key] == data[key] for key in data.keys()]):
                        item = Item()
                        item.data = dict(zodb_item.data)
                        item.uids = dict(zodb_item.uids)
                        results.add(item)
            return len(results), list(results)
        return (0, [])


    def delete(self, uid_name, uid_value):
        # update the uids dict
        del self.root[uid_name][uid_value].uids[uid_name]
        # delete the reference (other may exist in other containers)
        del self.root[uid_name][uid_value]
        transaction.commit()

    def put(self):
        raise NotImplementedError

zodb_storage = ZODBStorage()

class ItemZODBStorage(ZODBStorage):
    """Generic ZODB storage adapter for putting or deleting items
    """
    implements(IDatabase)
    adapts(IItem)
    def __init__(self, context):
        super(ItemZODBStorage, self).__init__()
        self.context = context

    def put(self, uid_name=None, uid_value=None):
        zodb_item = ZodbItem()
        # if we already have an uid,retrieve the existing object
        if self.context.uids is not None and len(self.context.uids) > 0:
            first_uid_name = self.context.uids.keys()[0]
            first_uid_value = self.context.uids[first_uid_name]
            zodb_item = self.root[first_uid_name][first_uid_value]

        # create the uid container
        if uid_name is not None and uid_name not in self.root:
            self.root[uid_name] = OOBTree()

        # if this is a new object, add it in the container
        if zodb_item.uids is None or len(zodb_item.uids) == 0:
            if uid_name is None or uid_value is None:
                raise ValueError('No uids')
            self.root[uid_name][uid_value] = zodb_item

        zodb_item.data = PersistentDict(self.context.data)
        zodb_item.uids = PersistentDict(self.context.uids)

        # update the uids
        if uid_name is not None and uid_value is not None:
            zodb_item.uids[uid_name] = uid_value
            self.root[uid_name][uid_value] = zodb_item

        transaction.commit()



