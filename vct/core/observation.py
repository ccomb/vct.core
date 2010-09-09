from zope.interface import implements
from zope.component import adapts
from vct.core.interfaces import IDatabase, IObservation

class Storage(object):
    """Storage adapter for observations
    We probably need to use a common base class
    """
    implements(IDatabase)
    adapts(IObservation)
    def __init__(self, context):
        self.context = context

    def save(self):
        print "save the observation somewhere"


class Observation(object):
    """a medical observation
    """
    implements(IObservation)
