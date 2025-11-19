from typing import Callable
# import trace

from ..utils.decorators import trace_function  # Note the two dots


@trace_function
def sum_original(
    # original `sum` function suggested at ch. 1.3.1 by leveraging trapezoidal rule
    term: Callable[[int | float], int | float],
    next_a: Callable[[int | float], int | float],
    a: float,
    b: int,
) -> int | float:
    return 0 if a > b else term(a) + sum_original(term, next_a, next_a(a), b)


@trace_function
def sum_iterative(
    term: Callable[[int | float], int | float],
    next_a: Callable[[int | float], int | float],
    a: int | float,
    b: int | float,
) -> int | float:
    def _iter(a: int | float, result: int | float):
        return result if a > b else _iter(next_a(a), term(a) + result)

    return _iter(a, 0)


def integral_original(f: Callable, a: int, b: int, dx: float) -> float:
    def add_dx(x):
        return x + dx

    return sum_original(f, add_dx, a + dx / 2, b) * dx


def cube(n):
    return n**3


def calculate_y(f, a, k, h):
    # calculate y factor of Simpson's rule equation
    return f(a + (k * h))


def integral_simpson(f, a, b, n) -> float:
    # Calculates integral by leveraging Simpson's rule

    h = (b - a) / n

    def term(x):
        if x == 0 or x == n:
            return calculate_y(f, a, x, h)
        if x % 2 == 0:
            return 2 * calculate_y(f, a, x, h)
        return 4 * calculate_y(f, a, x, h)

    def inc(x):
        return x + 1

    return sum_original(term, inc, 0, n) * (h / 3)


if __name__ == "__main__":
    # tracer = trace.Trace(trace=True, count=True)
    print(f"Testing recursive summation: {sum_original(cube, lambda x: x + 1, 0, 10)}")
    # tracer.runfunc(sum_original, cube, lambda x: x + 1, 0, 10)
    print(f"Testing iterative summation: {sum_iterative(cube, lambda x: x + 1, 0, 10)}")
    # tracer.runfunc(sum_iterative, cube, lambda x: x + 1, 0, 10)
    #
    # Here is output of the program:
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 0, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 1, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 2, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 3, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 4, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 5, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 6, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 7, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 8, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 9, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 10, 10) kwargs: {}
    # Calling sum_original with args: (<function cube at 0x7efd0ea27100>, <function <lamb
    # da> at 0x7efd0ea272e0>, 11, 10) kwargs: {}
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Exiting sum_original
    # Testing recursive summation: 3025
    # Calling sum_iterative with args: (<function cube at 0x7efd0ea27100>, <function <lam
    # bda> at 0x7efd0ea272e0>, 0, 10) kwargs: {}
    # Exiting sum_iterative
    # Testing iterative summation: 3025
