from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        left = 0
        right = 1

        while left < len(nums):
            if right < len(nums):
                if nums[left] + nums[right] < target:
                    count += 1
                right += 1
            else:
                left += 1
                right = left + 1
        return count