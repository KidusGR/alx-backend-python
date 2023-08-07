#!/usr/bin/env python3
""" Python async  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine"""

    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
