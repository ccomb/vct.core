from zope.component import getGlobalSiteManager
from vct.core.item import Item
from vct.core.issue import Issue
from vct.core.action import Action
from vct.core.patient import Patient
from vct.core.careprovider import CareProvider
from vct.core.agent import Agent
from vct.core.observation import Observation
from vct.core.db import zodb

# component registry
gsm = getGlobalSiteManager()
gsm.registerAdapter(zodb.ItemZODBStorage)
gsm.registerUtility(zodb.zodb_storage)


