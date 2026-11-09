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

        if self.low >= 0 and self.high >= 0 and other.low >= 0 and other.high >= 0:
            return Interval(self.low * other.low, self.high * other.high)
        if self.low >= 0 and self.high >= 0 and other.low < 0 and other.high >= 0:
            return Interval(self.high * other.low, self.high * other.high)
        if self.low >= 0 and self.high >= 0 and other.low < 0 and other.high < 0:
            return Interval(self.high * other.low, self.low * other.high)
        if self.low < 0 and self.high >= 0 and other.low >= 0 and other.high >= 0:
            return Interval(self.low * other.high, self.high * other.high)
        if self.low < 0 and self.high >= 0 and other.low < 0 and other.high < 0:
            return Interval(self.high * other.low, self.low * other.low)
        if self.low < 0 and self.high < 0 and other.low >= 0 and other.high >= 0:
            return Interval(self.low * other.high, self.high * other.low)
        if self.low < 0 and self.high < 0 and other.low < 0 and other.high >= 0:
            return Interval(self.low * other.high, self.low * other.low)
        if self.low < 0 and self.high < 0 and other.low < 0 and other.high < 0:
            return Interval(self.high * other.high, self.low * other.low)

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


def make_center_percent(c, p):
    width = c * p
    return Interval(c - width, c + width)


def percent(interval):
    return round(interval.width / (center(interval) * 0.01))


def center(interval):
    return (interval.low + interval.high) / 2


if __name__ == "__main__":
    i1 = make_center_percent(6.8, 0.1)
    i2 = make_center_percent(4.7, 0.05)
    print("We've got two intervals", i1, i2)
    print(f"width of first interval: ±{i1.width:.2f}, it's center is {center(i1):.2f}, it's percent: {percent(i1)}")
    print(f"width of second interval: ±{i2.width:.2f}, it's center is {center(i2):.2f}, it's percent: {percent(i2)}")
