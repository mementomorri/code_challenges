from collections import namedtuple


Pair = namedtuple('Pair', 'head tail')


def to_list(pair: Pair):
    if is_empty(pair):
        return []

    res = []
    pair_len = length(pair) + 1
    current_pair = pair

    for _ in range(pair_len):
        res.append(current_pair.head)
        current_pair = current_pair.tail

    return res


def is_empty(items: Pair | list):
    if isinstance(items, list):
        return True if items else False
    return items.tail is None


def length(items: Pair):
    return 1 + length(items.tail) if not is_empty(items) else 0


def reverse(items: Pair):
    items_len = length(items)
    if items_len <= 1:
        return items

    reversed = Pair(items.head, None)
    for _ in range(items_len):
        items = items.tail
        reversed = Pair(items.head, reversed)

    return reversed


if __name__ == "__main__":
    test_list = Pair(1, Pair(4, Pair(9, None)))
    print("reversing list [1, 4, 9]:", reverse(test_list))
    print(to_list(reverse(test_list)))
