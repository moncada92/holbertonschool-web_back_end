#!/usr/bin/env python3
""" let's duck type an iterable object"""

from typing import Iterable, List, Sequence, Union, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return sequence list """
    return [(i, len(i)) for i in lst]
