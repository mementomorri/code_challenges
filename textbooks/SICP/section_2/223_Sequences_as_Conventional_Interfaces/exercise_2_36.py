# all sequences are assumed to the same in length


def accumulate(op, initial, seq):
    return initial if not seq else op(seq[0], accumulate(op, initial, seq[1:]))


def dummy_accumulate_n(op, init, seqs):
    result = []
    seq_len = len(seqs[0])
    for i in range(seq_len):
        result.append(init)

    for seq in seqs:
        for i in range(seq_len):
            result[i] += seq[i]
    return result


def accumulate_n(op, init, seqs):
    return [accumulate(op, init, list(map(lambda x: x[i], seqs))) for i in range(len(seqs) - 1)]


if __name__ == '__main__':
    test_sequence = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    test_result = accumulate_n(lambda a, b: a + b, 0, test_sequence)
    # expected result here is (22, 26, 30)
    print(test_result)
