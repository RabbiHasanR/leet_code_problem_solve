from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 0
        sorted_keys = sorted(result, key=result.get, reverse=True)[:k]
        return sorted_keys