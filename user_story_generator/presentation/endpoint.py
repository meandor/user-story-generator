import logging

from flask import Flask, Response, jsonify


def start_server() -> Flask:
    logging.info("Starting server")
    app = Flask(__name__)

    @app.route("/health")
    def ping() -> Response:
        return jsonify({"status": "ok"})

    return app
