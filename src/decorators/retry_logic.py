import time
import functools
from typing import Callable, Type, Any, Tuple
import logging
import random

logger = logging.getLogger(__name__)


def retry(
    attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """

    Retry decorator fot handling transient failures.

    Args:
        attempts (int): Number of times to retry the function.
        delay (float): Initial delay between retries.
        backoff (float): Backoff factor for exponential backoff.
        exceptions (Tuple[Type[Exception], ...]): Tuple of exceptions to catch.

    Returns:
        Callable: The decorated function.

    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(
                        f"[{func.__name__}] Attempt {attempt} failed with exception {e}"
                    )
                    if attempt == attempts:
                        logger.critical(
                            f"[{func.__name__}] All {attempts} attempts failed. Raising exception."
                        )
                        raise
                    sleep_time = random.uniform(0, current_delay)
                    logger.info(
                        f"[{func.__name__}] Sleeping for {sleep_time:.2f}s before retry..."
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper

    return decorator
