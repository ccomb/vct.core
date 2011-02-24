from vct.core.item import Item
from zope.interface import implements
from zope.component import adapts
import colander, deform
from zope.interface import Interface
from vct.core.role import ROLES #XXX retrieve the role list from the db
import colander

class IUser(Interface):
    pass


class UserSchema(colander.Schema):
    """schema of a user
    """
    username = colander.SchemaNode(colander.String(),
                                title=u'User Name',
                                description=u'User Name')
    password = colander.SchemaNode(colander.String(),
                               title=u'Password',
                               description=u'Password',
                               widget=deform.widget.CheckedPasswordWidget())
    roles = colander.SchemaNode(deform.Set(),
                                 widget=deform.widget.CheckboxChoiceWidget(values=ROLES))


class User(Item):
    """a user in the current server
    """
    implements(IUser)
    schema = UserSchema()


class IUserPreferences(Interface):
    pass


class UserPreferencesSchema(colander.Schema):
    language = colander.SchemaNode(colander.String(),
                                   title=u'preferred language',
                                   validator=colander.OneOf(
                                       [u'english', u'french', u'spanish',
                                        u'german', u'greek', u'turkish']))
    initial_patient_view = colander.SchemaNode(colander.String(),
                                               title=u'Initial Patient View')


class UserPreferences(object):
    """adapter for user preferences
    """
    implements(IUserPreferences)
    adapts(IUser)
    #def __init__(self):
    #    self.language = 'english'
    #

