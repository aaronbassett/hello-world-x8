import falcon


class NCCOView:
    def on_get(self, req, resp):
        """Handles GET requests"""
        ncco = {"action": "talk", "text": "Hello World from Falcon"}

        resp.media = ncco


api = falcon.API()
api.add_route("/ncco", NCCOView())
