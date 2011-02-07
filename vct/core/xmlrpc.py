from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from SimpleXMLRPCServer import SimpleXMLRPCServer
from vct.core.interfaces import IItem
import multiprocessing, socket, sys
import colander, deform

class XMLRPCRequestHandler(SimpleXMLRPCRequestHandler):
    # Restrict to a particular path.
    rpc_paths = ('/RPC2',)


from zope.component import getUtility
from vct.core.db.interfaces import IDatabase

class Methods(object):
    """expose the database through xmlrpc

    TODO : remove this class, and change IDatabase to reflect this ??
    """
    def get_by_uid(self, uid_name, uid_value, model='item'):
        Model = getUtility(IItem, model)
        return IDatabase(Model()).get(uid=(uid_name, uid_value))

    def get_by_data(self, data, model='item'):
        Model = getUtility(IItem, model)
        return IDatabase(Model()).get(data=data)

    def put(self, uid_name, uid_value, data, model='item'):
        Model = getUtility(IItem, model)
        item = Model()
        if data is not None:
            if item.schema is not None:
                try:
                    item.data = item.schema.deserialize(data)
                except colander.Invalid, e:
                    return e.asdict()
            else:
                item.data = data
        return IDatabase(item).put(uid_name, uid_value)

    def delete(self, uid_name, uid_value, model='item'):
        Model = getUtility(IItem, model)
        IDatabase(Model()).delete(uid_name, uid_value)
        return 0

    def get_schema(self, name):
        """return a definition of the schema
        """
        model = getUtility(IItem, name)
        schema_dict = {}
        for field in model.schema:
            schema_dict[field.name] = dict([
                (name, value)
                for (name,value) in field.__dict__.items()
                if not name.startswith('_')
                ])
            schema_dict[field.name]['typ'] = field.typ.__class__.__name__.lower()
            schema_dict[field.name]['widget'] = field.widget.__class__.__name__.lower()
            schema_dict[field.name]['default'] = field.default.__class__.__name__.lower()
            del schema_dict[field.name]['missing'] # XXX not yet supported
        return schema_dict

    def get_form(self, model_name, format, data=None):
        """return a ready to use form for the given model,
        using the given format and given data.
        """
        Model = getUtility(IItem, model_name)
        model = Model()
        if format == 'html':
            myform = deform.Form(model.schema, buttons=('submit',))
            if data is not None:
                try:
                    myform.validate(data)
                except deform.ValidationFailure, e:
                    return e.render()
            return myform.render()
        else:
            raise NotImplementedError

    def login(self, login, password):
        """check the login and password and returns a token
        """
        Model = getUtility(IItem, 'user')
        number, users = IDatabase(Model()).get(uids={'username':login})
        assert(number==1)
        user = users[0]
        if password == user.data['password']:
            token = IDatabase(Token()).put()
            return token
        else:
            return False
        

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





