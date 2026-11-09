def accumulate(op, initial, seq):
    return initial if not seq else op(seq[0], accumulate(op, initial, seq[1:]))


def horner_eval(x, coeffs):
    return accumulate(lambda a, b: a + x * b, 0, coeffs)
    # here a is an-1 and b is an


if __name__ == '__main__':
    print(horner_eval(2, [1, 3, 0, 5, 0, 1]))
