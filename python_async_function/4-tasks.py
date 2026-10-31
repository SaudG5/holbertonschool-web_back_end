#!/usr/bin/env python3
"""Module that runs several wait_random tasks concurrently."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return the delays in completion order.

    The tasks run concurrently, so shorter delays finish first and the
    returned list is in ascending order without sorting.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for finished in asyncio.as_completed(tasks):
        delays.append(await finished)
    return delays
