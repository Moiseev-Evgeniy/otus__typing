"""
TODO:

Define a decorator `constructor_parameter` that accepts the type of Foo.
and return a wrapper function with the same signature as the constructor of Foo,
and function decorated by `constructor_parameter` can be called with an instance of Foo.
"""
from typing import Callable


def constructor_parameter[**P, T, R](cls: Callable[P, T]) -> Callable[[Callable[[T], R]], Callable[P, R]]:
    ...
