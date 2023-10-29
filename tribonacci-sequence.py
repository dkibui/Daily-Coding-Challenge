def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


def test_tribonacci():
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert tribonacci([1, 1, 1], 1) == [1]
    assert tribonacci([300, 200, 100], 0) == []
