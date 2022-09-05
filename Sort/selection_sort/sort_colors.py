# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0, n-1):
            index_min = i
            
            for j in range (i+1, n):
                if nums[j] < nums[index_min]:
                    index_min = j
            if index_min != i:
                nums[i], nums[index_min] = nums[index_min], nums[i]
        return nums

s = Solution()
nums = [2,0,2,1,1,0]
print(s.sortColors())