TOLERANCE = 0.00001


def fixed_point(f, first_guess, tolerance):
    def close_enough(a, b):
        return abs(a - b) < tolerance

    # def try_with(guess):
    #     next = f(guess)
    #     return next if close_enough(guess, next) else try_with(next)
    #
    # return try_with(first_guess)

    # Same as above
    x = first_guess
    while not close_enough(f(x), x):
        x = f(x)

    return x


if __name__ == "__main__":
    print(
        "Showing fixed point of golden ratio with x -> 1 + 1/x",
        fixed_point(lambda x: 1 + 1 / x, 1, TOLERANCE),
    )
    # Produces the result 1.6180371352785146
