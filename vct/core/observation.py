from vct.core.item import Item
from zope.interface import implements
import colander, deform
from zope.interface import Interface

class IObservation(Interface):
    pass

class ObservationSchema(colander.Schema):
    """schema of an observation
    """
    date = colander.SchemaNode(colander.DateTime(),
                               title=u'Date, time',
                               description=u'Date and time')
    title = colander.SchemaNode(colander.String(),
                                title=u'Title',
                                description=u'The title of the item')
    text = colander.SchemaNode(colander.String(),
                               title=u'content',
                               description=u'observation content',
                               widget=deform.widget.RichTextWidget(),
                               required=False)
    status = colander.SchemaNode(colander.String(),
                                 title=u"status",
                                 description=u"status of the action",
                                 required=False)
    link = colander.SchemaNode(colander.String(),
                               title=u"Link",
                               description=u'(Link to an external annex)',
                               required=False)

class Observation(Item):
    """a medical observation
    """
    implements(IObservation)
    schema = ObservationSchema()

