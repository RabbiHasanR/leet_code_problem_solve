# First Solution 
# time complexity for this solution O(n^2)
# space complexity for this solution O(1)
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         for index, num in enumerate(nums):
#             # check nums contain num:
#             for matchNum in nums[index+1:]:
#                 if num == matchNum:
#                     return True
#         return False


# Second Solution
# time complexity for this solution O(nlogn)
# space complexity for this solution O(1)
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         sort_nums = sorted(nums)
#         p, n = 0, 1
        
#         while n < len(sort_nums):
#             if sort_nums[p]==sort_nums[n]:
#                 return True
#             else:
#                 p = n
#             n+=1
#         return False


#third solution
# time complexity for this solution O(n)
# space complexity for this solution O(n)

class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

s = Solution()
nums = [1,2,3,1]
print(s.containsDuplicate(nums))