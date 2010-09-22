from zope.interface import Interface

class IItem(Interface):
    """medical item interface
    """

class IDatabase(Interface):
    """Interface for the database access
    """


class IObservation(Interface):
    """interface of an observation
    """


class IGroup(Interface):
    """interface of an object providing group features
    """
