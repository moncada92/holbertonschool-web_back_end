#!/usr/bin/env python3
""" Complex type - function """

from typing import Callable


def make_multiplier(multipler: float) -> Callable[[float], float]:
    """ return mutliply with function"""
    def func(number: float) -> float:
        return number * multipler

    return func
