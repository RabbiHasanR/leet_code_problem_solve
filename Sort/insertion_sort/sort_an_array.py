# Given an array of integers nums, sort the array in ascending order.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104


# time: O(n^2)
# space: O(1)

# solve using insertion sort algorithm but time limit exceed not excepted


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            item = nums[i]
            j = i - 1
            
            while j >= 0 and nums[j] > item:
                nums[j + 1] = nums[j]
                j = j -1
                nums[j + 1] = item
        return nums