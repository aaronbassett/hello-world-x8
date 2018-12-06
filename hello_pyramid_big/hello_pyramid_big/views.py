# views.py

from pyramid.view import view_config, view_defaults


@view_defaults(renderer="json")
class NCCOViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name="ncco")
    def ncco(self):
        return [{"action": "talk", "text": "Hello World from Pyramid"}]
