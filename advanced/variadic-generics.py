"""
TODO:

Define an `Array` type that supports element-wise addition of arrays with identical dimensions and types.
"""


class Array[*T]:
    def __add__(self, other: "Array[*T]") -> "Array[*T]":
        ...
