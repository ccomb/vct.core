from vct.core.item import Item
from zope.interface import implements
import colander, deform
from zope.interface import Interface
from vct.core.group import GROUPS #XXX retrieve the group list from the db
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
    groups = colander.SchemaNode(deform.Set(),
                                 widget=deform.widget.CheckboxChoiceWidget(values=GROUPS))


class User(Item):
    """a user in the current server
    """
    implements(IUser)
    schema = UserSchema()

