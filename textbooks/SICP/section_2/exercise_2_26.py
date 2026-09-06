# Output will look the same as using pairs,
# but structurally they are different.
# Although, I'm not sure there is
# much of a difference.

if __name__ == '__main__':
    X = [1, 2, 3]
    Y = [4, 5, 6]

    extended_y = X.copy()
    extended_y.extend(Y)
    print('append(x, y)', extended_y)

    print('pair(x, y)', [X, Y])

    print('list(x, y)', [X, Y, None])  # Same as previous
