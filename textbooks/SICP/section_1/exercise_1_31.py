from typing import Callable
import math
# import trace


def product(f: Callable, a: int | float, b: int | float) -> int | float:
    """function that returns the product of the values of a function at points over a given range."""

    # def _iter(a: int | float, result: int | float):
    #     return result if a > b else _iter(a + 1, result * f(a))
    #
    # return _iter(a, 1)

    result = 1
    stop_b = math.floor(b + 1)

    for a in range(1, stop_b):
        result *= f(a)

    return result


def factorial(n):
    return product(lambda x: x, 1, n)


if __name__ == "__main__":
    print(f"testing factorial: {factorial(10)}")
