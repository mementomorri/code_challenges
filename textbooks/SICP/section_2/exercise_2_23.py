# My implementation of for_each is
# similar to how Java's forEach behaves.
# But solution in textbook is different. It
# suggests a simpler implementation, just
# imitating the behavior of forEach,
# but not changing ebjects in place.


def for_each(items, func):
    for idx, item in enumerate(items):
        items[idx] = func(item)


if __name__ == '__main__':
    test_list1 = [1, 2, 3, 4, 5]
    for_each(test_list1, lambda x: print(x))
    print(test_list1)

    test_list2 = [1, 2, 3, 4, 5]
    for_each(test_list2, lambda x: x * x)
    print(test_list2)
