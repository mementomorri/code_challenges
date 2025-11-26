def cont_frac(n, d, k):
    """Computes the continued fraction representation of a given rational number."""
    result = 0
    for i in range(k, 0, -1):
        result = n(i) / (d(i) + result)

    return result


def cont_frac_rec(n, d, k):
    def fraction(i):
        if i == 0:
            return 0
        return n(i) / (d(i) + fraction(i - 1))

    return fraction(k)


def calculate_d(i):
    if i == 2:
        return 2
    if i > 2 and (i - 2) % 3 == 0:
        k = (i - 2) // 3
        return 2 * (k + 1)
    return 1


if __name__ == "__main__":
    print(
        "Checking approximation e, based on Euler's expansion",
        2 + cont_frac(lambda x: 1, calculate_d, 11),
    )
    # Looks almost correct, first 3 digits are right
