from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict()
        for i, num in enumerate(nums):
            if num in table:
                diff = table[num] - i
                if abs(diff) <= k:
                    return True
            table[num] = i
        return False
