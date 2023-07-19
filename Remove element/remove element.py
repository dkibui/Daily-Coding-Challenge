nums = [2, 2, 3, 0, 4, 2]
k = 2


def remove_element(nums, val):
    k = 0
    for i, n in enumerate(nums):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return nums


a = remove_element(nums, k)
print(a)
