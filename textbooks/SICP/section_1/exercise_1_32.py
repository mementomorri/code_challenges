def accumulate(combiner, null_value, term, a, next, b):
    if a > b:
        return null_value

    return combiner(term(a), accumulate(combiner, null_value, term, next(a), next, b))


def accumulate_iter(combiner, null_value, term, a, next, b):
    def iter(a, b):
        return combiner(term(a), iter(next(a), b) if a < b else null_value)

    return iter(a, b)


def inc(x):
    return x + 1


def cube(x):
    return x * x * x


def sum_cubes(a, b):
    return accumulate(lambda x, y: x + y, 0, cube, a, inc, b)


def sum_cubes_iterative(a, b):
    return accumulate_iter(lambda x, y: x + y, 0, cube, a, inc, b)


def factorial(n):
    return accumulate(lambda x, y: x * y, 1, lambda x: x, 1, lambda x: x + 1, n)


if __name__ == "__main__":
    print(f"sum_cubes(1, 10): {sum_cubes(1, 10)}")
    print(f"sum_cubes iterative(1, 10): {sum_cubes_iterative(1, 10)}")
    print(f"factorial(10): {factorial(10)}")
