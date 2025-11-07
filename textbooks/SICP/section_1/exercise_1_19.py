# Write a fuction decorator that prints current state of the variables
# when the function is called.


def print_state(func):
    def wrapper(*args, **kwargs):
        print(
            "a:",
            args[0],
            "b:",
            args[1],
            "p:",
            args[2],
            "q:",
            args[3],
            "count:",
            args[4],
            "Result:",
            func(*args, **kwargs),
        )
        return func(*args, **kwargs)

    return wrapper


def is_even(n):
    return n % 2 == 0


def fib(n):
    return fib_iter(1, 0, 0, 1, n)


# @print_state
def fib_iter(a, b, p, q, count):
    if count == 0:
        return b
    elif is_even(count):
        return fib_iter(a, b, p * p + q * q, p * q + p * q + q * q, count / 2)
    else:
        return fib_iter(b * q + a * q + a * p, b * p + a * q, p, q, count - 1)


if __name__ == '__main__':
    target_fib = int(input("Enter N fib number you want to find: "))
    print("The result is: ", fib(target_fib))
