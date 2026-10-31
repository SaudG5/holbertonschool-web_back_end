#!/usr/bin/env python3
"""Module providing a basic asynchronous coroutine that waits randomly."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds and return it.

    The delay is a float drawn uniformly from the range [0, max_delay].
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
