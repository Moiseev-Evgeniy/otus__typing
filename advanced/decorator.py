"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""
from typing import Callable


def decorator(message: str):
    def wrap[T: Callable](func: T) -> T:
        return func
    return wrap
