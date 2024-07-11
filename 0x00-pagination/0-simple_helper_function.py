#!/usr/bin/env python3
"""
define function called index_range that takes 2 args: page and page number
returns tuple with start index and end index
"""
def index_range(page: int, page_size: int) -> tuple:
    """
        my method
    """
    return ((page - 1) * page_size, page * page_size)
