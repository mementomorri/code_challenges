from random import randint
import time
from functools import wraps


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


def timed_prime_test(n: int) -> bool:
    print(f"Testing {n} for primality...")
    return start_prime_test(n, time.time())


def start_prime_test(n: int, start_time: float) -> bool:
    return report_prime(time.time() - start_time) if is_prime(n) else False


def report_prime(elapsed_time: float) -> bool:
    print(" *** ")
    print(f"Time elapsed: {elapsed_time} seconds")
    return True


def track_elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)  # Call the function
        end_time = time.perf_counter()  # End the timer
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Elapsed time for '{func.__name__}': {elapsed_time:.6f} seconds")
        return result

    return wrapper


if __name__ == "__main__":
    print("Larger than 1,000:")
    for _ in range(10):
        timed_prime_test(randint(1000, 9999))
    print("\nLarger than 10,000:")
    for _ in range(10):
        timed_prime_test(randint(10000, 99999))
    print("\nLarger than 100,000:")
    for _ in range(10):
        timed_prime_test(randint(100000, 999999))
