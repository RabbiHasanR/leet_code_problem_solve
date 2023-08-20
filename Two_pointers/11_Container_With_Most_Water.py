from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
    

        # brute force

        # res = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         area = (j - i) * min(height[i], height[j])
        #         res = max(res, area)
        # return res

        