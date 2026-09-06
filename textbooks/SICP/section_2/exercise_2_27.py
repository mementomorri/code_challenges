# Simple variation would look like this:


def deep_reversed(x: list) -> list:
    return x[::-1]


# I guess that's the benefits
# of using Python.


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    print(a)  # [[1, 2], [3, 4]]
    print(deep_reversed(a))  # [[3, 4], [1, 2]]
