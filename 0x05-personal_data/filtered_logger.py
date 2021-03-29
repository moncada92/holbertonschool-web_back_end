#!/usr/bin/env python3
"""filtered logger"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    filter_datum function
        # . -> match a character
        # + -> match more than one
        # ? -> repeat the next text of the match
    """
    for field in fields:
        print(f'{field}={redaction}{separator}')
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
