def square_tree(tree):
    result = []
    if tree is None:
        return None
    if not isinstance(tree, list):
        return tree * tree
    return [square_tree(tree[0]), square_tree(tree[1])]


def square_tree_using_maps(tree):
    return list(map(lambda x: x * x if not isinstance(x, list) else square_tree_using_maps(x), tree))


if __name__ == '__main__':
    print(square_tree([1, [2, [3, 4], [5]], [6, 7]]))
    print(square_tree_using_maps([1, [2, [3, 4], [5]], [6, 7]]))
