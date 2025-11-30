from typing import Callable

DX = 0.00001


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


def average(x, y, z):
    return (x + y + z) / 2


def smooth(f: Callable) -> Callable:
    return lambda x: average(f(x), f(x + DX), f(x - DX))


def n_fold_smooth(f: Callable, n: int) -> Callable:
    return repeated(smooth, n)(f)


if __name__ == "__main__":
    print(n_fold_smooth(square, 2)(5))  # 56.2500000003
