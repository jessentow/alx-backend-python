#!/usr/bin/env python3
"""This returns a function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function"""
    def mtp(n: float) -> float:
        """Returns the product"""
        return multiplier * n
    return mtp
