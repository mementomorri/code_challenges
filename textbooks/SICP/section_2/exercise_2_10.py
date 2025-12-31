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
        if other.low <= 0 or other.high <= 0:  # Basically, if any part of the interval
            # is negative or zero, then trow error
            return ZeroDivisionError("division by zero in one of the components")

        return self * Interval(1 / other.high, 1 / other.low)

    @property
    def width(self):
        return abs(self.high - self.low) / 2


if __name__ == "__main__":
    i1 = Interval(6.1, 7.5)
    i2 = Interval(4.45, 4.95)
    intervals_sum = i1 + i2
    intervals_mul = i1 * i2
    width_sum = i1.width + i2.width
    print("We've got two intervals", i1, i2)
    print(f"width of first interval: ±{i1.width:.2f}")
    print(f"width of second interval: ±{i2.width:.2f}")
    print(f"sum of width: ±{width_sum:.2f}")
    print("summation:", intervals_sum, f"and respective width: ± {intervals_sum.width:.2f}")
    print("multiplication", intervals_mul, f"and respective width: ± {intervals_mul.width:.2f}")
    # There is too much of the width after multiplication
