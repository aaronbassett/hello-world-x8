from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import json

app = Sanic("nexmo_app")


class NCCOAsyncView(HTTPMethodView):
    async def get(self, request):
        return json([{"action": "talk", "text": "Hello World from Sanic"}])


app.add_route(NCCOAsyncView.as_view(), "/ncco")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
