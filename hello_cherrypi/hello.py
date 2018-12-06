import cherrypy


class NCCOView(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return [{"action": "talk", "text": "Hello World from CherryPy"}]


if __name__ == "__main__":
    cherrypy.quickstart(NCCOView(), "/ncco")
