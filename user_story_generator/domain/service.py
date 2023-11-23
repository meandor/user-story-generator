import logging

from user_story_generator.domain.types import InferenceFn, AnswerFn


def generate_answer_fn(inference_fn: InferenceFn) -> AnswerFn:
    def answer_fn(prompt: str) -> str:
        logging.info("Generating answer")
        return inference_fn(prompt)

    logging.info("Done generating answer")

    return answer_fn
