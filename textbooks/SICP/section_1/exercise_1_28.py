import random


def miller_rabin(n: int):
    def expmod(b: int, exp: int, m: int):
        if exp == 0:
            return 1
        if exp % 2 == 0:
            return (trivial_test(expmod(b, exp // 2, m), m) ** 2) % m
        return (b * expmod(b, exp - 1, m)) % m

    def trivial_test(r: int, m: int) -> int:
        if r == 1 or r == m - 1:
            return r
        if (r**2) % m == 1:
            return 0
        return r

    def try_it(a):
        return expmod(a, n - 1, n) == 1

    return try_it(random.randint(1, n - 1))


def do_miller_rabit_test(n: int, times: int):
    if times == 0:
        return True
    if miller_rabin(n):
        return do_miller_rabit_test(n, times - 1)
    return False


if __name__ == "__main__":
    print("Testing Miller-Rabin test with Carmichael numbers...")
    carmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341]
    for n in carmichael_numbers:
        print(f"Miller-Rabin test for {n}: {do_miller_rabit_test(n, 10)}")

    print("Testing Miller-Rabin test with correct prime numbers...")
    correct_primes = (2, 3, 5, 7, 11, 13, 17)
    for n in correct_primes:
        print(f"Miller-Rabin test for {n}: {do_miller_rabit_test(n, 10)}")
