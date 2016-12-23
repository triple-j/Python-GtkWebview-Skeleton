import os.path
import cherrypy

from WebServer import Application

class Server(object):

    def __init__(self, root_path, port=8000):

        cherrypy.config.update({'server.socket_port': port})

        conf = {
            '/': {
                'tools.sessions.on': True,
                'tools.staticdir.root': root_path
            },
            '/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.normpath('./Assets/Public'),
            }
        }

        webapp = Application(root_path)
        cherrypy.tree.mount(webapp, '/', config=conf)
        cherrypy.engine.start()

    def stop(self):
        print('Stop Server')
        cherrypy.engine.stop()

