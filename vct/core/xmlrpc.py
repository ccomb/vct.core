from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from SimpleXMLRPCServer import SimpleXMLRPCServer
from vct.core import Item
from vct.core.interfaces import IModel
import multiprocessing, socket, sys

class XMLRPCRequestHandler(SimpleXMLRPCRequestHandler):
    # Restrict to a particular path.
    rpc_paths = ('/RPC2',)


from zope.component import getUtility
from vct.core.db.interfaces import IDatabase

class Methods(object):
    """expose the database through xmlrpc

    TODO : remove this class, and change IDatabase to reflect this ??
    """
    def __init__(self):
        self.database = getUtility(IDatabase)
    def get_by_uid(self, uid_name, uid_value):
        return self.database.get(uid=(uid_name, uid_value))
    def get_by_data(self, data):
        return self.database.get(data=data)
    def put(self, uid_name, uid_value, data):
        item = Item()
        item.data = data
        IDatabase(item).put(uid_name, uid_value)
        return 0
    def delete(self, uid_name, uid_value):
        getUtility(IDatabase).delete(uid_name, uid_value)
        return 0

    def get_model(self, name):
        """return a definition of the model
        """
        interface = getUtility(IModel, name)
        model = {}
        for field_name in interface:
            field = interface[field_name]
            model[field.__name__] = dict([
                (name, value)
                for (name,value) in field.__dict__.items()
                if not name.startswith('_') and name != 'interface'
                ])
            model[field.__name__]['type'] = field.__class__.__name__.lower()
        return model





class Server(object):
    """The vct.core server
    """
    def __init__(self, host, port):
        print 'listening on %s:%s' % (host, port)
        self.server = SimpleXMLRPCServer((host, port),
                            requestHandler=XMLRPCRequestHandler,
                            allow_none=True)
        self.server.register_introspection_functions()
        self.server.register_instance(Methods())


    def start(self, daemon=False):
        self.process = multiprocessing.Process(target=self.server.serve_forever)
        self.process.daemon = daemon
        self.process.start()

    def stop(self):
        # Run the server's main loop
        self.process.terminate()

server = None

def start():
    host = 'localhost'
    port = 8000
    if len(sys.argv) == 2 and ':' in sys.argv[1]:
        host = sys.argv[1].split(':')[0]
        port = int(sys.argv[1].split(':')[1])

    server = Server(host, port)
    server.start()





