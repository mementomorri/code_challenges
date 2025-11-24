from math import log


TOLERANCE = 0.00001


def fixed_point(f, first_guess, tolerance):
    def close_enough(a, b):
        return abs(a - b) < tolerance

    x = first_guess
    step = 0
    while not close_enough(f(x), x):
        print("Current guess:", x)
        x = f(x)
        step += 1

    print("Total number of steps:", step)

    return x


def fixed_point_wtih_avera_damping(f, first_guess, tolerance):
    def close_enough(a, b):
        return abs(a - b) < tolerance

    x = first_guess
    step = 0
    while not close_enough(f(x), x):
        print("Current guess:", x)
        x = (x + f(x)) / 2
        step += 1

    print("Total number of steps:", step)

    return x


if __name__ == "__main__":
    print(
        "Fixed point of x -> log(1000) / log(x) without average damping",
        fixed_point(lambda x: log(1000) / log(x), 2, TOLERANCE),
    )
    # Total number of steps: 33
    print(
        "Fixed point of x -> log(1000) / log(x) with average damping",
        fixed_point_wtih_avera_damping(lambda x: log(1000) / log(x), 2, TOLERANCE),
    )
    # Total number of steps: 9
    #
    # Although, results are the same, the average damping is more efficient
