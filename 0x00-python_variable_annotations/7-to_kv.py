#!/usr/bin/env python3
"""This returns a tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string k and float v as arguments
    and returns a tuple.
    """
    return (k, (v ** 2))
