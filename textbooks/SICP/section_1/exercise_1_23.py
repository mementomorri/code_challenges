import time


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
    return report_prime(time.time() - start_time) if is_prime(n) else False


def report_prime(elapsed_time: float) -> bool:
    print(" *** ")
    print(f"Time elapsed: {elapsed_time} seconds")
    return True


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
        "search_for_primes(1000000, 10000000):",
        search_for_primes((1000000, 10000000)),
    )
