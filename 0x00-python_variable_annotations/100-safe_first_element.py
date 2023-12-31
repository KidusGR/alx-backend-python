#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Arguments:
            lst: Any data type

        Returns:
            None or first element
    """
    if lst:
        return lst[0]
    else:
        return None
