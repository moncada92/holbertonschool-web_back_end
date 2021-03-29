#!/usr/bin/env python3
"""filtered logger"""

from typing import List
import re
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Constructor
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        format function
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    filter_datum function
        # . -> match a character
        # + -> match more than one
        # ? -> repeat the next text of the match
    """
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
    get_logger function
    source: https://realpython.com/python-logging/
    """
    # name of the logger
    logger = logging.getLogger("user_data")
    # set level to INFO
    logger.setLevel(logging.INFO)
    # propagate message
    logger.propagate = False
    # create the handle
    c_handler = logging.StreamHandler()
    # change format
    c_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    # add handler
    logger.addHandler(c_handler)
    return logger
