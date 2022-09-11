# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

# Example 1:

# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
 

# Constraints:

# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.

# first solution 
# time: O(logn)
# space: O(1)

# class Solution:
#     def dominantIndex(self, nums: List[int]) -> int:
#         arr = nums[:]
#         arr.sort(reverse=True)
#         if arr[1] == 0:
#             return nums.index(arr[0])
#         if (arr[0] // arr[1]) >= 2:
#             return nums.index(arr[0])
#         return -1

# second solution
# tiem: O(n)
# space: O(1)

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        for i in nums:
            if i!= largest and i * 2 > largest:
                return -1
        return nums.index(largest)

s = Solution()
nums = [1,2,3,4]
print(s.dominantIndex(nums))