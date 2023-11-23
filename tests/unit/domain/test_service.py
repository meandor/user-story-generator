from unittest.mock import MagicMock

from user_story_generator.domain import service


def test_return_answer():
    inference_fn_mock = MagicMock()
    inference_fn_mock.return_value = "foo"
    testee = service.generate_answer_fn(inference_fn_mock)

    actual = testee("bar")
    expected = "foo"

    assert expected == actual
    inference_fn_mock.assert_called_with("bar")


def test_return_another_answer():
    inference_fn_mock = MagicMock()
    inference_fn_mock.return_value = "foobar"
    testee = service.generate_answer_fn(inference_fn_mock)

    actual = testee("foo")
    expected = "foobar"

    assert expected == actual
    inference_fn_mock.assert_called_with("foo")
