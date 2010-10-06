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

class IDatabase(Interface):
    """Interface for the database access
    """
    def get(uid=None, data=None):
        """retrieve objects from the database
        """

    def put(uid_name=None, uid_value=None):
        """save an object in the database
        """

    def delete(uid_name, uid_value):
        """delete an object from the database
        """

class IObservation(Interface):
    """interface of an observation
    """


class IGroup(Interface):
    """interface of an object providing group features
    """
