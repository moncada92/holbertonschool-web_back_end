#!/usr/bin/env python3
""" complex type string and int/float to tulple """

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple """
    return k, v**2
