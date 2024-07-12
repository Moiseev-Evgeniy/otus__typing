"""
TODO: Annotate function `f` and `g`, to make tests pass.
"""
from collections.abc import Sequence


def f(a: list[int | str]):
    pass


def g(a: Sequence[int | str]):
    pass


# or

# f_types = list[int | str]
# g_types = list[int] | list[int | str] | str | bytes | tuple[int, str, int]
#
#
# def f(a: f_types) -> None:
#     pass
#
#
# def g(a: g_types) -> None:
#     pass
