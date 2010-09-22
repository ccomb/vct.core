from zope.interface import implements
from vct.core.interfaces import IGroup

class Agent(object):
    pass


class AgentGroup(object):
    implements(IGroup)
