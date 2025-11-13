from typing import Callable


def sum_original(
    # original `sum` function suggested at ch. 1.3.1 by leveraging trapezoidal rule
    term: Callable[[int | float], int | float],
    next_a: Callable[[int | float], int | float],
    a: float,
    b: int,
) -> int | float:
    return 0 if a > b else term(a) + sum_original(term, next_a, next_a(a), b)


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
    print("Testing with original integral...")
    print(f"integral of x^3 from 0 to 1 is {integral_original(cube, 0, 1, 0.01)}")
    # 0.24998750000000042
    # print(f"integral of x^3 from 0 to 1 is {integral_original(cube, 0, 1, 0.001)}")
    # Above one exceeds the maximum recursion depth
    print("Testing with integral by Simpson's rule...")
    print(f"integral of x^3 from 0 to 1 is {integral_simpson(cube, 0, 1, 100)}")
    # 0.24999999999999992
    # print(f"integral of x^3 from 0 to 1 is {integral_simpson(cube, 0, 1, 1000)}")
    # Above one exceeds the maximum recursion depth
