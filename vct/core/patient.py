from vct.core.item import Item
from zope.interface import Interface, implements
import colander, deform

class IPatient(Interface):
    pass

genders = {'M': 'Male', 'F': 'Female', '?': 'Unknown'}


class Items(colander.SequenceSchema):
    item = colander.SchemaNode(colander.String(),
                               title=u'Item')


class PatientSchema(colander.Schema):
    firstname = colander.SchemaNode(colander.String(),
                                    title=u'First name')
    lastname = colander.SchemaNode(colander.String(),
                                   title=u'Last name')
    birthdate = colander.SchemaNode(colander.Date(),
                                    title=u'Birth date')
    sex = colander.SchemaNode(colander.String(),
                              validator=colander.OneOf(genders.keys()),
                              widget=deform.widget.SelectWidget(values=genders.items()),
                              title=u'Sex')
    address = colander.SchemaNode(colander.String(),
                                  title=u'Address')
    postcode = colander.SchemaNode(colander.String(),
                                   title=u'Post code')

    items = Items(missing=[])


class Patient(Item):
    implements(IPatient)
    schema = PatientSchema()


