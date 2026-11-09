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


# asignment C


def is_blanced(mobile) -> bool:
    """
    By formal definition: A mobile is said to be balanced
    if the torque applied by its top-left branch is equal to
    that applied by its top-right branch (that is, if the
    length of the left rod multiplied by the weight hanging
    from that rod is equal to the corresponding product for
    the right side) and if each of the submobiles hanging
    off its branches is balanced.

    With that said, submobiles have to be balanced for mobile
    in general to be balanced and sum of weights on left and
    right must be equal. Let's have simplified version of a
    solution for this exercise, since perfect solution requires
    DFS, in my opinion. Will review it later, for better version.
    """
    total_weight_left = branch_structure(left_branch(mobile))
    if not isinstance(total_weight_left, int):
        total_weight_left = total_weight(total_weight_left)

    total_weight_right = branch_structure(right_branch(mobile))
    if not isinstance(total_weight_right, int):
        total_weight_right = total_weight(total_weight_right)

    return total_weight_left == total_weight_right


if __name__ == "__main__":
    simple_mobile = make_mobile(make_branch(1, make_mobile(make_branch(2, 2), make_branch(2, 2))), make_branch(1, 1))

    print(f"simple mobile: {simple_mobile}")
    print("structure of the simple test mobile:\n\t\t\t|\n\t\t|\t\t1\n\t2\t\t2")
    print("total weight of simple mobile is:", total_weight(simple_mobile))
    # [[1, [[2, 2], [2, 2]]], [1, 1]]
    #         |
    #       |  1
    #     2  2
    print("is simple mobile balanced?", is_blanced(simple_mobile))
