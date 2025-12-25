class Pair:
    def __init__(self, x, y):
        self.store = (2**x) * (3**y)

    def head(self):
        def helper(p):
            return helper(p / 2) + 1 if p % 2 == 0 else 0

        return helper(self.store)

    def tail(self):
        def helper(q):
            return helper(q / 3) + 1 if q % 3 == 0 else 0

        return helper(self.store)


if __name__ == "__main__":
    p = Pair(1, 2)
    print("Head:", p.head())
    print("Tail:", p.tail())
