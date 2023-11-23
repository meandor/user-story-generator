import logging
from typing import Any

from flask import Flask, Response, jsonify, request, make_response

from user_story_generator.data import model
from user_story_generator.domain import service

_PROMPT_KEY = "prompt"


def _is_valid_request(request: dict[str, Any]) -> bool:
    return bool(request.get(_PROMPT_KEY))


def start_server() -> Flask:
    logging.info("Starting server")
    app = Flask(__name__)
    inference_fn = model.generate_inference_fn()
    answer_fn = service.generate_answer_fn(inference_fn)

    @app.route("/user_story", methods=["POST"])
    def create_user_story() -> Response:
        data = request.get_json()
        if not _is_valid_request(data):
            response_body = {"error": "invalid request"}
            status_code = 400
            response = make_response(jsonify(response_body), status_code)
            return response

        prompt = data[_PROMPT_KEY]
        logging.info("Processing prompt")
        answer = answer_fn(prompt)
        return jsonify({"answer": answer})

    @app.route("/health")
    def ping() -> Response:
        return jsonify({"status": "ok"})

    return app
