def subarray_sums(numbers, queries):
    # prefix_sums[i] = sum of numbers[0:i], 0 <= i <= len(numbers)
    prefix_sums = [0]
    for number in numbers:
        prefix_sums.append(prefix_sums[-1] + number)
    return [(prefix_sums[end] - prefix_sums[start]) for start, end in queries]
