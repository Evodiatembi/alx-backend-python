#!/usr/bin/env python3
"""A function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier float uses callable from typing
    """
    return lambda x: x * multiplier
