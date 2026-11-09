from collections import namedtuple

Point = namedtuple('Point', 'low high')


class Interval(Point):
    @property
    def width(self):
        return abs(self.high - self.low) / 2

    def upper_bound(self):
        return self.high

    def lower_bound(self):
        return self.low

    def __str__(self):
        return f"[{self.low:.2f}, {self.high:.2f}]"

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


def make_center_percent(c: int | float, p: int | float):
    width = c * p
    return Interval(c - width, c + width)


def percent(interval: Interval):
    return round(interval.width / (center(interval) * 0.01))


def center(interval: Interval):
    return round((interval.low + interval.high) / 2, 2)


def par1(r1: Interval, r2: Interval):
    return r1 * r2 / (r1 + r2)


def par2(r1: Interval, r2: Interval):
    ONE = Interval(1, 1)
    return ONE / (ONE / r1 + ONE / r2)


if __name__ == "__main__":
    i1 = make_center_percent(6.8, 0.1)
    i2 = make_center_percent(4.7, 0.05)
    intervals_sum = i1 + i2
    intervals_mul = i1 * i2
    width_sum = i1.width + i2.width
    print("We've got two intervals", i1, i2)
    print(f"width of first interval: ±{i1.width:.2f}")
    print(f"width of second interval: ±{i2.width:.2f}")
    print(f"sum of width: ±{width_sum:.2f}")
    print("summation:", intervals_sum, f"and respective width: ± {intervals_sum.width:.2f}")
    print("multiplication", intervals_mul, f"and respective width: ± {intervals_mul.width:.2f}\n")
    pr1 = par1(i1, i2)
    pr2 = par2(i1, i2)
    print(
        f"parallel resistance, first formula: {pr1}, center: {center(pr1)}, width: {pr1.width:.2f}, percent: {percent(pr1)}"
    )
    print(f"second formula: {pr2}, center: {center(pr2)}, width: {pr2.width:.2f}, percent: {percent(pr2)}")
    print(f"Deviding first interval by itself: {i1/i1}")
    print(f"Deviding first interval by second: {i1/i2}")
    # The expression A/A is interesting, because if the interval
    # is meant to represent a specific (albeit imprecisely known) value,
    # the result should be exactly 1 (width 0), whereas the interval
    # division will result in an interval with positive width.
    # Multiple occurrences of the same term are not recognized as
    # such in the approaches above and thus they will suffer from this problem.
