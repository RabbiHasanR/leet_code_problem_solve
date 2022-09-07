# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000

# time: O(n^2)
# space: O(1)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n):
            item = nums[i]
            j = i - 1
            while j >= 0 and (nums[j] % 2 != 0 and item % 2 == 0):
                nums[j+1] = nums[j]
                j = j -1
                nums[j+1] = item
                    
        return nums

s = Solution()
nums = [3,1,2,4]
print(s.sortArrayByParity(nums))