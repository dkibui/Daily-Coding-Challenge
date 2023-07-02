def sum_pairs(numbers, s):
    seen = set()
    for num in numbers:
        difference = s - num
        if difference in seen:
            return [difference, num]
        seen.add(num)
    return None
