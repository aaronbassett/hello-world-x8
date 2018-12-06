from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(renderer="json")
def ncco(request):
    return [{"action": "talk", "text": "Hello World from Pyramid"}]


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("ncco", "/ncco")
        config.add_view(ncco, route_name="ncco", renderer="json")
        app = config.make_wsgi_app()

    server = make_server("0.0.0.0", 8000, app)
    server.serve_forever()
