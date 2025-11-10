import math
import random
import time

# from functools import wraps


def smallest_divisor(n: int):
    return find_devisor(n, 2)


def next_d(d: int) -> int:
    return d + 1 if d == 2 else d + 2


def find_devisor(n: int, d: int):
    if d * d > n:
        return n
    elif n % d == 0:
        return d
    else:
        return find_devisor(n, next_d(d))


def is_prime(n):
    return n == smallest_divisor(n)


def timed_prime_test(n: int, show_log=None) -> bool:
    if show_log:
        print(f"Testing {n} for primality...")
    return start_prime_test(n, time.time())


def start_prime_test(n: int, start_time: float) -> bool:
    return report_prime(time.time() - start_time) if fast_is_prime(n, 3) else False


def report_prime(elapsed_time: float) -> bool:
    print(" *** ")
    print(f"Time elapsed: {elapsed_time} seconds")
    return True


# def track_elapsed_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()  # Start the timer
#         result = func(*args, **kwargs)  # Call the function
#         end_time = time.perf_counter()  # End the timer
#         elapsed_time = end_time - start_time  # Calculate elapsed time
#         print(f"Elapsed time for '{func.__name__}': {elapsed_time:.6f} seconds")
#         return result
#
#     return wrapper


# Probabalistic approach with O(log n)


def fast_expt(b: int, exp: int):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return fast_expt(b, exp // 2) ** 2
    else:
        return b * fast_expt(b, exp - 1)


def expmod(b: int, exp: int, m: int):
    return fast_expt(b, exp) % m


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


def search_for_primes(search_rage: tuple[int, int], show_log=None) -> tuple[int]:
    result = list()
    prime_counter = 0
    for n in range(search_rage[0], search_rage[1]):
        if timed_prime_test(n, show_log):
            prime_counter += 1
            result.append(n)
            print(f"{prime_counter}-th primal number")

        if prime_counter >= 3:
            break
    return tuple(result)


if __name__ == "__main__":
    print("search_for_primes(1000, 10000):", search_for_primes((1000, 10000)))
    print("search_for_primes(10000, 100000):", search_for_primes((10000, 100000)))
    print("search_for_primes(100000, 1000000):", search_for_primes((100000, 1000000)))
    print(
        "search_for_primes(1000000, 10000000):", search_for_primes((1000000, 10000000))
    )

    # Alyssa's suggestion is correct at first sight:
    # her expmod function computes baseexp and then finds its remainder modulo m,
    # as required in the Fermat test.
    # However, for large bases, Alyssa's method will quickly bump
    # into limitations because Python uses from 30 to 64 bits to represent numbers,
    # following the double-precision floating point standard IEEE 754,
    # which says that floats are folding 64 bits of data.
    # When the numbers become so large that they cannot be represented
    # precisely any longer in this standard, the results become unreliable.
    # Even worse, the method might exceed the largest number that
    # can be represented in this standard, and the computation leads to an error.
    # For small bases, however, Alyssa's method may be even faster
    # than the original expmod function, because it will carry
    # out only one single remainder operation.
