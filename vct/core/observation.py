from vct.core.item import Item
from zope.interface import implements
import colander, deform
from zope.interface import Interface

class IObservation(Interface):
    pass

class ObservationSchema(colander.Schema):
    """schema of an observation
    """
    date = colander.SchemaNode(colander.Date(),
                               title=u'Date',
                               description=u'Date and time')
    title = colander.SchemaNode(colander.String(),
                                title=u'Title',
                                description=u'The title of the item')
    text = colander.SchemaNode(colander.String(),
                               title=u'content',
                               description=u'observation content',
                               widget=deform.widget.RichTextWidget())
    status = colander.SchemaNode(colander.String(),
                                 title=u"status",
                                 description=u"status of the action")
    link = colander.SchemaNode(colander.String(),
                               title=u"Link",
                               description=u'(Link to an external annex)')

class Observation(Item):
    """a medical observation
    """
    implements(IObservation)
    schema = ObservationSchema()

