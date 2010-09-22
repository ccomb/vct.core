from zope.component import getGlobalSiteManager
from vct.core.item import Item
from vct.core.issue import Issue
from vct.core.action import Action
from vct.core.patient import Patient
from vct.core.careprovider import CareProvider
from vct.core.agent import Agent
from vct.core.observation import Observation
from vct.core import database

# component registry
gsm = getGlobalSiteManager()
gsm.registerAdapter(database.ItemZODBStorage)
gsm.registerUtility(database.zodb_storage)


