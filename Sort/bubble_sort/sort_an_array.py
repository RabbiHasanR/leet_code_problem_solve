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

# solve using bubble sort algorithm but time limit exceed not excepted


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            is_already_sorted = True
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_already_sorted = False
            if is_already_sorted:
                break
        return nums

s = Solution()
nums = [2,0,2,1,1,0]
print(s.sortArray())