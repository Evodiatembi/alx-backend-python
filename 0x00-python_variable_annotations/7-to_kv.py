#!/usr/bin/env python3
"""Function that converts a Python variable to a KV pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Tuple of strings, int and or floats
    Args: 
        k: a string
        v: int and or float
    Returns:
        Turple: k is a string and v a square of the int/float 
    """
    return (k, float(v**2))
