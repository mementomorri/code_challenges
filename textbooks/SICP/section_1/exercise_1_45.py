import math
from typing import Callable

DX = 0.0000001


def fixed_point(f, first_guess, tolerance):
    def close_enough(a, b):
        return abs(a - b) < tolerance

    x = first_guess
    step = 0
    while not close_enough(f(x), x):
        # print("Current guess:", x)
        x = f(x)
        step += 1

    print("Total number of steps:", step)

    return x


def average_damp(f: Callable) -> Callable:
    return lambda x: (x + f(x)) / 2


def inc(x: int) -> int:
    return x + 1


def double(f: Callable) -> Callable:
    return lambda x: f(f(x))


def compose(f: Callable, g: Callable) -> Callable:
    return lambda x: f(g(x))


def square(x: int) -> int:
    return x * x


def repeated(f: Callable, n: int) -> Callable:
    if n == 0:
        return lambda x: x
    return lambda x: repeated(f, n - 1)(f(x))


def repeated_with_compose(f: Callable, n: int) -> Callable:
    if n == 0:
        return lambda x: x
    return compose(f, repeated_with_compose(f, n - 1))


def average(x, y):
    return (x + y) / 2


def nth_root(n: int, root_power: int) -> float:
    return fixed_point(
        repeated(average_damp, math.floor(math.log2(n)))(
            lambda y: root_power / math.exp(y)
        ),
        1,
        DX,
    )


if __name__ == "__main__":
    print(
        f"Trying to findout n-th root using repeated: root base 2 of 25: {nth_root(25, 2)}"
    )
