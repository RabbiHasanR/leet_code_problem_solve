from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prev = None
        count = 0
        track = 0
        result = 0
        while count < len(nums):
            if prev == None:
                prev = nums[count]
                track += 1
            else:
                if nums[count] - prev == 1:
                    prev = nums[count]
                    track += 1
                if nums[count] - prev > 1:
                    if track > result:
                        result = track
                    prev = nums[count]
                    track = 1 
            count += 1
        if track > result: 
            return track
        return result