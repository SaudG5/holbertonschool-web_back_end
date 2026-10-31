#!/usr/bin/env python3
"""Module that runs several wait_random coroutines concurrently."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delays in completion order.

    Because the coroutines run concurrently, the shortest delays finish
    first, so the returned list ends up in ascending order without sorting.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for finished in asyncio.as_completed(coroutines):
        delays.append(await finished)
    return delays
