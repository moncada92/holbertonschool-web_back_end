#!/usr/bin/env python3
""" Complex type - function """

from typing import Callable, Union, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return mutliply with function"""
    def func(number: float) -> float:
        return number * multiplier

    return func
