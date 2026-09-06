# Since text-books implementation requires
# defenition of list as pairs
# and I'm lazy to do it, I use
# built-in list and map instead


def square_list_1(items):
    return [item * item for item in items]


def square_list_2(items):
    return list(map(lambda x: x * x, items))
