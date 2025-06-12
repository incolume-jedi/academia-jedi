"""Module API."""

import os

from fastapi import FastAPI
from redis import Redis

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = os.environ.get('REDIS_PORT', 6379)


app = FastAPI()
redis = Redis(host=redis_host, port=redis_port)


@app.get('/')
async def root() -> dict[str, str]:
    """Principal method.

    Returns:
        dict[str, str]: message getting.
    """
    redis.incr('hits-root')
    return {'message': 'Hello World'}


@app.get('/counter')
async def counter() -> dict[str, int]:
    """Counter access for API.

    Returns:
        int: Number of access.
    """
    redis.incr('hits-counter')
    return {
        'total hits': sum(int(x) for x in [redis.get('hits-root'), redis.get('hits-counter')]),
        'root hits': redis.get('hits-root'),
        'counter hits': redis.get('hits-counter')
    }
