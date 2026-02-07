from collections import namedtuple


Pair = namedtuple('Pair', 'head tail')


def is_empty(items: Pair | list):
    if isinstance(items, list):
        return True if items else False
    return items.tail is None


def length(items: Pair):
    return 1 + length(items.tail) if not is_empty(items) else 0


def last_pair(items: Pair):
    items_length = length(items)
    res = items
    for _ in range(items_length):
        res = res.tail
    return res


if __name__ == "__main__":
    print("the last pair of pairs list [1, 2, 3] is:", last_pair(Pair(1, Pair(2, Pair(3, None)))))
