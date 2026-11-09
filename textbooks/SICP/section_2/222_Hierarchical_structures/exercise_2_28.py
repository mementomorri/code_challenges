# Again, simplified version.
# Version with pairs would be like:
# for item in tree:
#     if isinstance(item, Pair) and not isinstance(item.tail, Pair):
#         res.extend([item.head, item.tail])
#         continue
#     res.append(item.head)
# or something similar, but not a big difference.


def fringe(tree):
    res = []
    for item in tree:
        if isinstance(item, list):
            res.extend(fringe(item))
            continue
        res.append(item)
    return res


if __name__ == "__main__":
    x = [[1, 2], [3, 4]]
    print(fringe(x))
    print(fringe([x, x]))
