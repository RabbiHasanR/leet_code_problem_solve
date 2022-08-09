# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# -1000 <= a, b <= 1000

# First solution
# time: O(n)
# space: O(1)

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         while b != 0:
#             carry = a & b
#             a = a ^ b
#             b = carry << 1
#         return a


# Second solution
# time: O(1)
# space: O(1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        l = [a,b]
        return sum(l)

sol = Solution()
a = 1
b = 2
print(sol.getSum(a, b))