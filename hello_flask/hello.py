from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ncco")
def ncco():
    return jsonify([{"action": "talk", "text": "Hello World from Flask"}])
