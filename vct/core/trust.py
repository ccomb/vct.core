from zope.interface import Interface, Attribute, implements
from zope.component import adapts

class ITrustable(Interface):
    """marker interface for object providing trust features
    """


class ITrust(Interface):
    """interface for the trust level
    """
    value = Attribute(u'the numerical trust value')
    level = Attribute(u'the trust identifier')

class Trust(object):
    """adapter giving the trustlevel
    """
    implements(ITrust)
    adapts(ITrustable)

    def __init__(self, context):
        self.context = context

    def get_levels(self):
        """FIXME : store in global
        """
        return self.context.data.get('trustlevels')

    def set_levels(self, levels):
        self.context.data['trustlevels'] = levels

    levels = property(get_levels, set_levels)


    def get_value(self, attr):
        return self.context.data.get('trustvalue')

    def set_value(self, attr, value):
        self.context.data['trustvalue'] = value

    def get_level(self, attr):
        level = self.context.data.get('trustlevel')
        if level is None:
            raise NotImplementedError


    def set_level(self, attr, level):
        self.context.data['trustlevel'] = level




