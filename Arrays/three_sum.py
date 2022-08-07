# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# first solution
# time: O(n^2)
# space: O(1) or O(n)

class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i , n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            left , right = i+1, len(nums)-1
            while left < right:
                three_sum = n + nums[left] + nums[right]
                    
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))
