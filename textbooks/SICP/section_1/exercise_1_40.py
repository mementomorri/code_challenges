from typing import Callable

DX = 0.00001


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


def deriv(f: Callable):
    return lambda x: (f(x + DX) - f(x)) / DX


def newton_transform(g: Callable):
    return lambda x: x - g(x) / deriv(g)(x)


def newtons_method(g: Callable, guess):
    return fixed_point(newton_transform(g), guess, 0.0001)


def cube(x):
    return x * x * x


def square(x):
    return x * x


def sqrt(x):
    return newtons_method(lambda y: square(y) - x, 1)


def cubic(a, b, c):
    """Declare a function cubic that can be used together with the newtons_method function in
    expressions of the form
    newtons_method(cubic(a, b, c), 1)
    to approximate zeros of the cubic x**3 + ax**2 + bx + c."""
    return lambda x: cube(x) + a * square(x) + b * x + c


if __name__ == "__main__":
    # print(deriv(cube)(5))  # 75.00014999664018
    print(newtons_method(cubic(1, 0, -1), 1))
