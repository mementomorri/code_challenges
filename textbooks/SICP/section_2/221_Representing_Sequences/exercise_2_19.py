US_COINS = [50, 25, 10, 5, 1]
UK_COINS = [100, 50, 20, 10, 5, 2, 1]


class Pair:
    def __init__(self, head: int | None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return f"Pair(head={self.head}, tail={self.tail})"


def to_list(pair: Pair):
    if is_empty(pair):
        return []

    res = []
    current_pair = pair

    while current_pair is not None:
        res.append(current_pair.head)
        current_pair = current_pair.tail

    return res


def to_pair(lst: list):
    if not lst:
        return Pair(None, None)

    res = Pair(lst[0], None)
    current_pair = res

    for v in lst[1:]:
        current_pair.tail = Pair(v, None)
        current_pair = current_pair.tail

    return res


def is_empty(items: Pair | list):
    if items is None:
        return True
    if isinstance(items, list):
        return not items

    return items.head is None


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


def count_change(amount: int, coins: list):
    return cc(amount, to_pair(coins))


def no_more(coins: Pair):
    return is_empty(coins)


def first_denominator(coins: Pair):
    return 0 if no_more(coins) else coins.head


def except_first_denomination(coins: Pair):
    if no_more(coins):
        return Pair(None, None)
    return coins.tail if coins.tail is not None else Pair(None, None)


def cc(amount: int, coins: Pair):
    if amount == 0:
        return 1
    elif amount < 0 or no_more(coins):
        return 0
    else:
        return cc(amount - first_denominator(coins), coins) + cc(amount, except_first_denomination(coins))


if __name__ == "__main__":
    print(to_pair(US_COINS))
    print("there are", count_change(100, US_COINS), "ways to make change for 100 cents")
    # there are 292 ways to make change for 100 cents
