from zope.interface import Interface, Attribute

class IItem(Interface):
    """common interface of item classes
    It allows to retrieve any class of type IItem, with its name
    (see __init__.py with registry configuration)
    """
    data = Attribute(u'Data of the record')
    uids = Attribute(u'Unique Identifiers of the record')
    schema = Attribute(u'Data Schema')
    version = Attribute(u'Version of the record')
