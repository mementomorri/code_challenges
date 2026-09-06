# If I got it correctly, exercise just requires me
# to select 7 from each list, that's simple enough, can be achieved
# just by sequence of correct indexes.
# With pairs that's no different though.

if __name__ == '__main__':
    a = [1, 3, [5, 7], 9]
    b = [[7]]
    c = [1, [2, [3, [4, [5, [6, 7]]]]]]

    print('list(1, 3, list(5, 7), 9):', a[2][1])
    print('list(list(7)):', b[0][0])
    print('list(1, list(2, list(3, list(4, list(5, list(6, 7)))))):', c[1][1][1][1][1][1])
