def tree_map(f, tree):
    return list(map(lambda x: tree_map(f, x) if isinstance(x, list) else f(x), tree))


if __name__ == '__main__':
    print(tree_map(lambda x: x * x, [1, [2, [3, 4], [5]], [6, 7]]))
