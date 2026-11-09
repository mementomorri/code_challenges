class Pair_original:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dispatch(self, m):
        if m == 0:
            return self.x
        elif m == 1:
            return self.y
        print("Error: Invalid dispatch. Argument should be either 0 or 1, but got:", m)
        return None

    def head(self):
        return self.dispatch(0)

    def tail(self):
        return self.dispatch(1)


def pair(x, y):
    return lambda m: m(x, y)


def head(z):
    return z(lambda p, q: p)


def tail(z):
    return z(lambda p, q: q)


if __name__ == "__main__":
    p = pair(1, 2)
    # We store a function in variable
    print("Head:", head(p))
    # Then we call for a function that returns
    # first argument
    print("Tail:", tail(p))
    # And then second argument
