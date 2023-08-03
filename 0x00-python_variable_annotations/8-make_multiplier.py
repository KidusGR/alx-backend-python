#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Arguments:
            multiplier: factor

        Returns:
            multiplication in float
    """

    def x(f: float) -> float:
        """ Get the second argument somthing like JS """
        return float(f * multiplier)

    return x
