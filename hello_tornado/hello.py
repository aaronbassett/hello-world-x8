import tornado.ioloop
import tornado.web
from tornado import escape
from tornado.escape import utf8


class NCCOHandler(tornado.web.RequestHandler):
    def write(self, chunk):
        chunk = escape.json_encode(chunk)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)

    def get(self):
        self.write([{"action": "talk", "text": "Hello World from Tornado"}])


def make_app():
    return tornado.web.Application([(r"/ncco", NCCOHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
