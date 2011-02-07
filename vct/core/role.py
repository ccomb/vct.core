
from zope.interface import Interface, Attribute, implements
from vct.core.item import Item
import colander

ROLES = [('admins', u'Administrators'),
          ('users', u'Users'),
          ('patients', u'Patients')]

class IRole(Interface):
    """interface of a role
    """


class RoleSchema(colander.Schema):
    """schema of a role
    """
    name = colander.SchemaNode(colander.String(),
                               title=u"Name",
                               description=u"Role Name")

class Role(Item):
    """ a role
    """
    implements(IRole)
    schema = RoleSchema()
