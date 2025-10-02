import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.decorators import retry

logging.basicConfig(level=logging.DEBUG)


def test_retry_happy_flow():
    @retry()
    def success(x: int):
        return x * 9

    result = success(2)
    assert result == 18


def test_retry_succeeds_after_retries():
    attempts = {"count": 0}

    @retry(attempts=3, delay=0.1, backoff=2.0)
    def flaky_function(x: int) -> int:
        if attempts["count"] < 1:
            attempts["count"] += 1
            raise ValueError("Transient error")
        return x * 2

    result = flaky_function(5)
    assert result == 10
