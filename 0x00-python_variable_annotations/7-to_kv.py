#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Arguments:
            k: String
            v: Union: Can be int or float

        Returns:
            Tuple with string and int or float
    """

    cncat: Tuple(str, Union[int, float])
    cncat = (k, v**2)

    return cncat
