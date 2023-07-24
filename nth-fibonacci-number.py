def fibonacci(n):
    pre, cur = 1, 1
    for _ in range(n - 2):
        nxt = pre + cur
        pre, cur = cur, nxt
    return cur


print(fibonacci(6))

# OR

# def fibonacci(n):
#     fibs = [1, 1]
#     while len(fibs) < n:
#         fibs.append(fibs[-1] + fibs[-2])
#     return fibs[-1]

# print(fibonacci(6))
