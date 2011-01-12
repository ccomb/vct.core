from zope.interface import Interface, Attribute
import zope.schema

class IModel(Interface):
    """ marker interface to distinguish model interfaces
    It allows to retrieve any interface of type IModel, with its name
    (see __init__.py with registry configuration)
    """


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
    date = zope.schema.Datetime(title=u'Date, time',
                                description=u'Date and time')
    title = zope.schema.TextLine(title=u'Title',
                                 description=u'The title of the item')
    text = zope.schema.Text(title=u'content',
                            description=u'observation content', required=False)
    status = zope.schema.TextLine(title=u"status",
                                  description=u"status of the action", required=False)
    image = zope.schema.Bytes(title=u"attached file",
                              description=u"attached file", required=False)
    link = zope.schema.TextLine(title=u"Link",
                                description=u'(Link to an external annex)',
                                required=False)




