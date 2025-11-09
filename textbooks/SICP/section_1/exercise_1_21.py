import math
import random


# Testing for primality with O(sqrt(n)) by using numbers' divisors
def smallest_divisor(n: int):
    return find_devisor(n, 2)


def find_devisor(n: int, d: int):
    if d * d > n:
        return n
    elif n % d == 0:
        return d
    else:
        return find_devisor(n, d + 1)


def is_prime(n):
    return n == smallest_divisor(n)


# Probabalistic approach with O(log n)
def expmod(b: int, exp: int, m: int):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return expmod(b, exp // 2, m) ** 2
    else:
        return (b * expmod(b, exp - 1, m)) % m


def fermat_test(n: int):
    def try_it(a: int):
        return expmod(a, n, n) == a

    return try_it(1 + math.floor(random.random() * (n - 1)))


def fast_is_prime(n: int, times: int):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_is_prime(n, times - 1)
    else:
        return False


if __name__ == "__main__":
    print("smallest_devisor(199):", smallest_divisor(199))  # 199
    print("smallest_devisor(1999):", smallest_divisor(1999))  # 1999
    print("smallest_devisor(19999):", smallest_divisor(19999))  # 7

    print("fast_is_prime(199, 2):", fast_is_prime(199, 2))  # True
    print("fast_is_prime(1999, 2):", fast_is_prime(1999, 2))  # True
    print("fast_is_prime(19999, 2):", fast_is_prime(19999, 2))  # False
