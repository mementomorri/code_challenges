def f(g):
    return g(2)


if __name__ == "__main__":
    print(f(lambda x: x * x))
    print(f(lambda x: x * (x + 1)))
    # print(f(f))
    # This leads us to:
    # f(f)
    # f(2)
    # 2(2)
    # Which raises an error since 2 is not callable
