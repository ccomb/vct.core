""" Module defining the group capability
"""
from zope.interface import Interface, Attribute

class IGroup(Interface):
    """interface of an object providing group features
    """
    name = Attribute(u"Group name")


class Group(object):
    """ a group
    """
    def __init__(self, name):
        self.name = name
