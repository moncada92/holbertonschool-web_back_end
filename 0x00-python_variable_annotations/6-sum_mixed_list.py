#!/usr/bin/env python3
""" complex types mixed list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum mixed values in list type int and float """
    return sum(mxd_lst)
