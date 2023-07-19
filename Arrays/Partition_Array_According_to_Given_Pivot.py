from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small_nums = []
        big_nums = []
        equal_nums = []

        for num in nums:
            if num < pivot:
                small_nums.append(num)
            elif num > pivot:
                big_nums.append(num)
            else:
                equal_nums.append(num)
        return small_nums + equal_nums + big_nums
        