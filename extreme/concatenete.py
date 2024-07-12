"""
TODO:

Suppose there's a function `foo`, whose first parameter can be anything.

You want to use `foo`, but want to restrict the first argument to be a `Person`.
You cannot modify `foo`, so you decide to write a function `transform`,
to transform `foo` into the function you want.
"""
from typing import Callable, Any, Concatenate


class Person:
    pass


def transform[T, **P](f: Callable[Concatenate[Any, P], T]):
    def wrapper(value: Person, *args: P.args, **kwargs: P.kwargs) -> T:
        return f(value, *args, **kwargs)

    return wrapper
