def make_mobile(left, right):
    return [left, right]


def make_branch(length, structure):
    return [length, structure]


# asignment A


def left_branch(mobile):
    if mobile:
        return mobile[0]
    return None


def right_branch(mobile):
    if mobile:
        return mobile[1]
    return None


def branch_length(branch):
    if branch:
        return branch[0]
    return None


def branch_structure(branch):
    if branch:
        return branch[1]
    return None


# asignment B


def total_weight(mobile):
    if isinstance(mobile, int):
        return mobile
    return total_weight(branch_structure(left_branch(mobile))) + total_weight(branch_structure(right_branch(mobile)))


if __name__ == "__main__":
    simple_mobile = make_mobile(make_branch(1, make_mobile(make_branch(2, 2), make_branch(2, 2))), make_branch(1, 1))

    print("total weight of simple mobile is:", total_weight(simple_mobile))
    # [[1, [[2, 1], [2, 1]]], [1, 1]]
