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


if __name__ == "__main__":
    print(
        "Iterative: Checking approximation with 1/φ:",
        cont_frac(lambda x: 1, lambda x: 1, 11),
    )
    # k = 4 would suffice
    print(
        "Recursive: Checking approximation with 1/φ:",
        cont_frac_rec(lambda x: 1, lambda x: 1, 11),
    )
