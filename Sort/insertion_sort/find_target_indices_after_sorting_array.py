# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100

# time: O(n^n)
# space: O(1)

class Solution:
    def insertion_sort_asc(self,nums):
        n = len(nums)
        for i in range(1,n):
            item = nums[i]
            j = i - 1
            while j>=0 and nums[j] > item:
                nums[j+1] = nums[j]
                j = j - 1
                nums[j+1] = item
        return nums
    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = self.insertion_sort_asc(nums)
        print(sorted_nums)
        return [i for i in range(len(sorted_nums)) if sorted_nums[i]==target]


s = Solution()
nums = [1,2,5,2,3]
target = 3
print(s.targetIndices(nums,target))