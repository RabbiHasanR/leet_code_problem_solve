from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = 0
        start = 0
        end = 0
        current_sum = 0

        while end < len(nums):
            current_sum = current_sum + nums[end]
            end = end + 1

            while start < end and current_sum >= target:
                current_sum = current_sum - nums[start]
                start = start + 1

                if min_length == 0:
                    min_length = end - start + 1
                else:
                    min_length = min(min_length, end - start + 1)
        return min_length