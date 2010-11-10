from zope.interface import Interface, Attribute

class IItem(Interface):
    """medical item interface.
    An item is just a placeholder for a dict of data,
    referenced with any number of uids.
    The uids attribute is a dict of uids:
    a uid for vct, a uid for a hospital, one for a laboratory, etc.
    """
    uids = Attribute(u'dict of uids')
    data = Attribute(u'dict of data')

class IObservation(Interface):
    """interface of an observation
    """



