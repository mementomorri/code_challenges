from typing import Callable


def inc(x: int) -> int:
    return x + 1


def double(f: Callable) -> Callable:
    return lambda x: f(f(x))


def compose(f: Callable, g: Callable) -> Callable:
    return lambda x: f(g(x))


def square(x: int) -> int:
    return x * x


if __name__ == "__main__":
    print(compose(square, inc)(6))  # 49
    # Basically, it first applies increment, then squaring,
    # so it is: (6 + 1) ** 2 = 49
