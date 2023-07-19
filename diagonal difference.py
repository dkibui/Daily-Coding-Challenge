def diagonal_difference(arr):
    n = len(arr)
    left = 0
    right = 0

    for i in range(n):
        l = arr[i][i]
        left += l
        r = arr[i][n - 1 - i]
        right += r

    return abs(left - right)


arr = [
    [9, 2, 4],
    [4, 5, 6],
    [10, 8, 2]
]
print(diagonal_difference(arr))
