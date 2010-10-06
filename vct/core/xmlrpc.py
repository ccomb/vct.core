from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from vct.core import Item

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()



from zope.component import getUtility
from vct.core.interfaces import IDatabase

class Database(object):
    """expose the database through xmlrpc
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


server.register_instance(Database())



##### Register pow() function; this will use the value of
##### pow.__name__ as the name, which is just 'pow'.
####server.register_function(pow)
####
##### Register a function under a different name
####def adder_function(x,y):
####    return x + y
####server.register_function(adder_function, 'add')
####
##### Register an instance; all the methods of the instance are
##### published as XML-RPC methods (in this case, just 'div').
####class MyFuncs:
####    def div(self, x, y):
####        return x // y
####
####server.register_instance(MyFuncs())


def start():
    # Run the server's main loop
    server.serve_forever()


