import cherrypy

class Application(object):

    def __init__(self, root_path):
        self.root_path = root_path

    @cherrypy.expose
    def index(self):
        return open(self.root_path + '/Assets/Application.html')
