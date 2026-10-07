def accumulate(op, initial, seq):
    # print(initial, seq)
    return initial if not seq else op(seq[0], accumulate(op, initial, seq[1:]))


def map_f(f, seq):
    return accumulate(lambda x, y: [f(x)] + y, [], seq)


def append(s1, s2):
    return accumulate(lambda x, y: x + y, [], [s1, s2])


def length(seq):
    return accumulate(lambda x, y: y + 1, 0, seq)


if __name__ == '__main__':
    print(map_f(lambda x: x + 1, [1, 2, 3]))
    print(append([1, 2, 3], [4, 5, 6]))
    print(length([1, 2, 3]))
    print(length([0, 0, 0]))
    print(length([]))
