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
    p1 = 0
    for n in range(1000, 10000):
        if timed_prime_test(n):
            p1 += 1
            print(f"{p1}-th primal number")

        if p1 >= 3:
            break

    print("\nLarger than 10,000:")
    p2 = 0
    for n in range(10000, 100000):
        if timed_prime_test(n):
            p2 += 1
            print(f"{p2}-th primal number")

        if p2 >= 3:
            break

    print("\nLarger than 100,000:")
    p3 = 0
    for n in range(100000, 1000000):
        if timed_prime_test(n):
            p3 += 1
            print(f"{p3}-th primal number")

        if p3 >= 3:
            break
