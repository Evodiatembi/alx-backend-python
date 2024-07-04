#!/usr/bin/env python3
"""A function with annotated parameters and
return values with appropriate types."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes  and return the length of a list of sequences.
    """
    return [(i, len(i)) for i in lst]
