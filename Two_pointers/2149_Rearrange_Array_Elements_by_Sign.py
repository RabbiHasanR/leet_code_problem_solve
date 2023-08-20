from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negetive = []
        positive = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negetive.append(num)
        result = []
        index = 0
        while index < len(negetive):
            result.append(positive[index])
            result.append(negetive[index])
            index += 1
        return result