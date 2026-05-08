import asyncio
import random
from functools import wraps
from config.settings import MAX_RETRIES, RETRY_DELAY


def get_random_user_agent(user_agents: list[str]) -> str:
    return random.choice(user_agents)


def async_retry(max_retries: int = MAX_RETRIES, delay: int = RETRY_DELAY):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
                    if attempt < max_retries:
                        await asyncio.sleep(delay * attempt)
                    else:
                        raise last_exception
        return wrapper
    return decorator