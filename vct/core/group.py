""" Module defining the group capability
"""
from zope.interface import Interface, Attribute, implements
from vct.core.item import Item
import colander

GROUPS = [('admins', u'Administrators'),
          ('users', u'Users'),
          ('patients', u'Patients')]

class IGroup(Interface):
    """interface of an object providing group features
    """


class GroupSchema(colander.Schema):
    """schema of a group
    """
    name = colander.SchemaNode(colander.String(),
                               title=u"Name",
                               description=u"Group Name")

class Group(Item):
    """ a group
    """
    implements(IGroup)
    schema = GroupSchema()
