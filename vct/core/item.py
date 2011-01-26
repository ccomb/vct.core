from zope.interface import implements
from vct.core.interfaces import IItem
import colander

class Item(object):
    """medical item interface.
    An item is just a placeholder for a dict of data,
    referenced with any number of uids.
    The uids attribute is a dict of uids:
    a uid for vct, a uid for a hospital, one for a laboratory, etc.
    """
    implements(IItem)
    data = None
    uids = None
    schema = None

    def __init__(self):
        self.data = {}
        self.uids = {}


