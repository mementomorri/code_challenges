"""
Define a better version of make_rat that handles both positive and negative arguments. The
function make_rat should normalize the sign so that if the rational number is positive, both
the numerator and denominator are positive, and if the rational number is negative, only the
numerator is negative.
"""


def gcd(a: int | float, b: int | float):
    return a if b == 0 else gcd(b, a % b)


class Pair:
    # Base class for pair of numbers
    def __init__(self, head: int | float, tail: int | float):
        self.head = head
        self.tail = tail

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail


def make_rat(n: int | float, d: int | float):
    # Simulate constructor for rational numbers
    g = gcd(n, d)
    return Pair(n / g, d / g)


def numer(x: Pair):
    # Return numerator of rational number
    return x.get_head()


def denom(x: Pair):
    # Return denominator of rational number
    return x.get_tail()


def add_rat(x: Pair, y: Pair):
    # Sum of rational numbers
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))


def sub_rat(x: Pair, y: Pair):
    # Difference of rational numbers
    return make_rat(numer(x) * denom(y) - numer(y) * denom(x), denom(x) * denom(y))


def mul_rat(x: Pair, y: Pair):
    # Multiplication of rational numbers
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def div_rat(x: Pair, y: Pair):
    # Division of rational numbers
    return make_rat(numer(x) * denom(y), denom(x) * numer(y))


def equal_rat(x: Pair, y: Pair):
    # Equality of rational numbers
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rat(x: Pair):
    print(f"{numer(x)} / {denom(x)}")


def enhaced_make_rat(n: int | float, d: int | float):
    # Enhanced version of make_rat that is sign aware
    if d < 0 and n > 0:
        return make_rat(-n, abs(d))
    return make_rat(n, abs(d))


if __name__ == "__main__":
    one_half = enhaced_make_rat(1, 2)
    print_rat(one_half)
    one_third = enhaced_make_rat(1, 3)
    print_rat(one_third)
    print_rat(add_rat(one_half, one_third))
    print_rat(mul_rat(one_half, one_third))
    print_rat(add_rat(one_third, one_third))

    neg_one_half = enhaced_make_rat(-1, 2)
    neg_one_third = enhaced_make_rat(1, -3)
    print_rat(neg_one_half)
    print_rat(neg_one_third)
