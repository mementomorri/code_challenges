from typing import Callable


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


if __name__ == "__main__":
    print(repeated(square, 2)(5))  # 625
    print(repeated_with_compose(square, 2)(5))  # 625
