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


# time: O(nlogn)
# space: O(1)

# solve using merge sort algorithm but time limit exceed not excepted

class Solution:
    
    def merge(self, a,b):
        merge_list = []
        len_a,len_b=len(a),len(b)
        index_a,index_b = 0,0
        while index_a < len_a and index_b < len_b:
            if a[index_a] < b[index_b]:
                merge_list.append(a[index_a])
                index_a += 1
            else:
                merge_list.append(b[index_b])
                index_b += 1
        if index_a < len_a:
            merge_list.extend(a[index_a:])
        if index_b < len_b:
            merge_list.extend(b[index_b:])
        return merge_list
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)

s = Solution()
nums = [2,0,2,1,1,0]
print(s.sortArray())