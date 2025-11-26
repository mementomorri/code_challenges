def cont_frac(n, d, k):
    """Computes the continued fraction representation of a given rational number."""
    result = 0
    for i in range(k, 0, -1):
        result = n(i) / (d(i) + result)

    return result


def tan_cf(x, k):
    n = lambda i: i == 1 if x else -x * x
    d = lambda i: 2 * i - 1
    return cont_frac(n, d, k)
