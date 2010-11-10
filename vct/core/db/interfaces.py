from zope.interface import Interface

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


