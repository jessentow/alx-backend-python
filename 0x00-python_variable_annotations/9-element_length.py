#!/usr/bin/env python3
"""This returns list"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This returns values with appropriate types"""
    return [(i, len(i)) for i in lst]
