# The result list is reversed in the
# first program because the argument
# list is traversed in the given order,
# from first to last, but squares are added
# successively to the front of the answer list
# via pair. That's why it doesn't work with my
# implementation, there is no pairs currently,
# although it would fail the same if there is
# pairs.
# The last element of the list is the last
# one to be added to the answer and thus ends
# up as the first element of the result list.
# Second implementation behaves the same.


def square_list(items):
    def iter(things, answer):
        if not things:
            return answer
        else:
            return iter(things[1:], answer + [things[0] * things[0]])

    return iter(items, [])


if __name__ == '__main__':
    print(square_list([1, 2, 3, 4, 5]))
