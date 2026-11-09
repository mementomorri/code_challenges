# Implementation without pairs looks like this.
# Pairs itself not essencial to understand
# trees concept, although it takses
# more thinking to implement them with pairs.


def count_leaves(x):
    if isinstance(x, list):
        return sum(map(count_leaves, x))
    else:
        return 1


if __name__ == '__main__':
    print(len([[1, 2], [3, 4]]))
    print(count_leaves([[1, 2], [3, 4]]))
    print(count_leaves([1, [2, [3, 4]]]))
