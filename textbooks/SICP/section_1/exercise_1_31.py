from typing import Callable
import math
# import trace


def product(f: Callable, a: int, b: int | float, c=None) -> int | float:
    """function that returns the product of the values of a function at points over a given range."""

    # def _iter(a: int | float, result: int | float):
    #     return result if a > b else _iter(a + 1, result * f(a))
    #
    # return _iter(a, 1)

    result = a
    stop_b = math.floor(b + 1)
    if c is None:
        c = 1

    for n in range(a, stop_b, c):
        result *= f(n)

    return result


def factorial(n):
    return product(lambda x: x, 1, n)


def product_pi(n: int) -> float:
    """Calculate approximation to Pi using Wallis method."""

    def multiply_by_self(n):
        return n + n

    return (product(lambda x: x + 2, 2, n, 2)) / product(multiply_by_self, 3, n, 2)


if __name__ == "__main__":
    print(f"testing factorial of 10: {factorial(10)}")
    # print(f"testing product_pi: {product_pi(10)}")
