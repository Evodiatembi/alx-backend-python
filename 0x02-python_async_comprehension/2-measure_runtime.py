#!/usr/bin/env python3
"""Asynchronous measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather
"""
from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Checks execution time
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
