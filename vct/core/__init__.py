from zope.component import getGlobalSiteManager
from vct.core import observation

getGlobalSiteManager().registerAdapter(observation.Storage)


