from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result_sum = 0
        items = zip(*[sorted(g) for g in grid])
        for item in items:
            result_sum += max(item)
        return result_sum