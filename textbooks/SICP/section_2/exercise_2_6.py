zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))


def add_1(n):
    return lambda f: lambda x: f(n(f)(x))


def plus(n, m):
    return lambda f: lambda x: f(n(f)(x)) + m(f)(x)


def church_to_num(c):
    return c(lambda n: n + 1)(0)


if __name__ == "__main__":
    three = plus(one, two)
    print(church_to_num(three))
