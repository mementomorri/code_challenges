from collections import namedtuple

Point = namedtuple('Point', 'x y')


class Interval(Point):
    def upper_bound(self):
        return self.x

    def lower_bound(self):
        return self.y

    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __add__(self, other):
        return Interval(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        p1 = self.x * other.x
        p2 = self.x * other.y
        p3 = self.y * other.x
        p4 = self.y * other.y
        return Interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

    def __truediv__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        if other.x == 0 or other.y == 0:
            return ZeroDivisionError("division by zero in one of the components")
        return self * Interval(1 / other.y, 1 / other.x)


if __name__ == "__main__":
    i1 = Interval(1, 2)
    i2 = Interval(3, 4)
    print("We've got two intervals", i1, i2)
    print("summation:", i1 + i2)
    print("multiplication", i1 * i2)
    print("division:", i1 / i2)
