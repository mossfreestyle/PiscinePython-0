#!/usr/bin/env python3

from typing import Iterable, Callable, TypeVar, List

T = TypeVar("T")

def ft_filter(function: Callable[[T], bool], iterable: Iterable[T]) -> List[T]:
    return [item for item in iterable if function(item)]