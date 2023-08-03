#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Arguments:
            input_list: float numbers

        Returns:
            Sum of the float numbers
    """

    result: float = 0

    for x in input_list:
        result += x

    return result
