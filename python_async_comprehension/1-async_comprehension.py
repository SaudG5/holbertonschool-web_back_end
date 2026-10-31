#!/usr/bin/env python3
"""Module that collects random numbers with an async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator and return them.

    The values are gathered with an asynchronous list comprehension.
    """
    return [i async for i in async_generator()]
