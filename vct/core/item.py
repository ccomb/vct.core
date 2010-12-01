from vct.core.interfaces import IItem
from zope.interface import implements

class Item(object):
    implements(IItem)
    data = None
    uids = None

    def __init__(self):
        self.data = {}
        self.uids = {}


