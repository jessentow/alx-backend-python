#!/usr/bin/env python3
"""This returns sum as float"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats
    Returns sum as float
    """
    return sum(mxd_lst)
