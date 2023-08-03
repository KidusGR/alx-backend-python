#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
        Arguments:
            lst: Sequence of list

        Returns:
            List of tuple of sequence of integers
    """

    return [(i, len(i)) for i in lst]
