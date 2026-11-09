def accumulate(op, initial, seq):
    return initial if not seq else op(seq[0], accumulate(op, initial, seq[1:]))


def map_f(f, seq):
    return accumulate(lambda x, y: [f(x)] + y, [], seq)


def count_leaves(t):
    return accumulate(
        lambda x, y: x + y, 0, map_f(lambda sub_t: count_leaves(sub_t) if isinstance(sub_t, list) else 1, t)
    )


if __name__ == '__main__':
    print(count_leaves([[[1, 2], 3, 4], [[5, 6], 7, 8]]))
