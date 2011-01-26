from zope.interface import Interface

class IItem(Interface):
    """ marker interface to distinguish item classes
    It allows to retrieve any class of type IItem, with its name
    (see __init__.py with registry configuration)
    """

