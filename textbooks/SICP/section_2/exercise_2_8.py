from collections import namedtuple

Point = namedtuple('Point', 'low high')


class Interval(Point):
    def upper_bound(self):
        return self.high

    def lower_bound(self):
        return self.low

    def __str__(self):
        return f"[{self.low:.2f},{self.high:.2f}]"

    def __add__(self, other):
        return Interval(self.low + other.low, self.high + other.high)

    def __sub__(self, other):
        return Interval(self.low - other.low, self.high - other.high)

    def __mul__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        p1 = self.low * other.low
        p2 = self.low * other.high
        p3 = self.high * other.low
        p4 = self.high * other.high
        return Interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

    def __truediv__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        if other.low == 0 or other.high == 0:
            return ZeroDivisionError("division by zero in one of the components")
        return self * Interval(1 / other.high, 1 / other.low)


if __name__ == "__main__":
    i1 = Interval(6.1, 7.5)
    i2 = Interval(4.45, 4.95)
    print("We've got two intervals", i1, i2)
    print("summation:", i1 + i2)
    print("subtraction:", i1 - i2)
    print("multiplication", i1 * i2)
    print("division:", i1 / i2)
