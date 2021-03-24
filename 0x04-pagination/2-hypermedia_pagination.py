#!/usr/bin/env python3

import csv
import math
from typing import List
from math import ceil


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        get_range = index_range(page, page_size)
        _start = get_range[0]
        _end = get_range[1]
        return self.dataset()[_start: _end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        get_range = index_range(page, page_size)
        _start = get_range[0]
        _end = get_range[1]
        data = self.dataset()[_start: _end]

        total_page = ceil(self.dataset().__len__() / page_size)

        return {
          'page_size': page_size,
          'page': page,
          'data': data,
          "next_page": page + 1 if page < total_page else None,
          "prev_page": page - 1 if page > 1 else None,
          'total_pages': total_page
        }
