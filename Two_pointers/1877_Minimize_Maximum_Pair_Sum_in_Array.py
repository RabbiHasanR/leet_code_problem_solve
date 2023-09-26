from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        first = 0
        last = len(nums) - 1
        max_sum = 0
        while first < len(nums):
            max_sum = max(max_sum, nums[first] + nums[last])
            first += 1
            last -= 1
        return max_sum
            