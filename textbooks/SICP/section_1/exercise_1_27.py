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


def carmichael(n: int) -> bool:
    """Return True if a^n ≡ a (mod n) for all a in 2..n-1 (direct Fermat-style check)."""

    def expmod(base: int, exp: int, m: int) -> int:
        base %= m
        result = 1
        while exp > 0:
            print(f"base={base}, exp={exp}, m={m}, result={result}")
            if exp % 2 == 1:  # test least-significant bit via remainder
                result = (result * base) % m
            base = (base * base) % m
            exp = exp // 2  # divide by 2 instead of bit-shift
        return result

    if n < 3:
        return False
    for a in range(2, n):
        if expmod(a, n, n) != a % n:
            return False
    return True


if __name__ == "__main__":
    print("Testing fermat theorem lazyly with Carmichael numbers...")
    carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341]
    for n in carmichael_numbers:
        print(f"Fermat test for {n}: {fermat_test(n)}")

    print("Testing fermat theorem with Carmichael numbers as the exercise says...")
    carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341]
    for n in carmichael_numbers:
        print(f"Fermat test for {n}: {carmichael(n)}")
        break
