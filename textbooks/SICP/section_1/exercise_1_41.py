from typing import Callable


def inc(x: int) -> int:
    print(f"Current value: {x}")
    return x + 1


def double(f: Callable) -> Callable:
    return lambda x: f(f(x))


if __name__ == "__main__":
    print(double(double(double))(inc)(5))  # 21
    # 21 = 5+16 = 5 + (16 * 2) = 5 + (8 * 2 * 2) = 5 + (4 * 2 * 2 * 2)
    print(double(inc)(5))  # 7
