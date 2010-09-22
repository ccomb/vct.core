from vct.core.item import Item
from zope.interface import implements
from vct.core.interfaces import IObservation

class Observation(Item):
    """a medical observation
    """
    implements(IObservation)
