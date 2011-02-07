from zope.component import getGlobalSiteManager
from vct.core.item import Item
from vct.core.issue import Issue
from vct.core.action import Action
from vct.core.patient import Patient
from vct.core.careprovider import CareProvider
from vct.core.agent import Agent
from vct.core.user import User
from vct.core.observation import Observation
from vct.core.interfaces import IItem
from vct.core.db import zodb
from vct.core import trust
from os.path import dirname, join
import logging

try:
    SERVER_NAME = open(join(dirname(dirname(dirname(__file__))), 'server_name.txt')).read().strip()
except:
    logging.warn(u"You should define a server name in 'server_name.txt'")
    SERVER_NAME = 'server1'

# component registry
gsm = getGlobalSiteManager()
gsm.registerAdapter(zodb.ItemZODBStorage)

gsm.registerAdapter(trust.Trust)

gsm.registerUtility(Item, IItem, 'item')
gsm.registerUtility(Observation, IItem, 'observation')
gsm.registerUtility(User, IItem, 'user')
