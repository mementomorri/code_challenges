def subsets(s):
    if s is None:
        return None
    else:
        rest = subsets(s[1:])
        rest.extend(list(map(lambda x: [s[0], x], rest)))
        return rest


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
