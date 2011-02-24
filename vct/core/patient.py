from vct.core.item import Item
from zope.interface import Interface, implements
import colander

class IPatient(Interface):
    pass


class PatientSchema(colander.Schema):
    id = colander.SchemaNode(colander.String(),
                             title=u'id')
    firstname = colander.SchemaNode(colander.String(),
                                    title=u'First name')
    lastname = colander.SchemaNode(colander.String(),
                                   title=u'Last name')
    birthdate = colander.SchemaNode(colander.Date(),
                                    title=u'Birth date')
    sex = colander.SchemaNode(colander.String(),
                                    validator=colander.OneOf(['Male', 'Female', 'Unknown']),
                                    title=u'Sex')
    address = colander.SchemaNode(colander.String(),
                                   title=u'Address')
    postcode = colander.SchemaNode(colander.String(),
                                   title=u'Post code')


class Patient(Item):
    implements(IPatient)
    schema = PatientSchema()


