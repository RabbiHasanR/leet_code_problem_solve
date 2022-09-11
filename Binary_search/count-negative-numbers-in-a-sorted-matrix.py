# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
 

# Follow up: Could you find an O(n + m) solution?

# first solution
# time: O(n^2)
# space: O(1)

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         count = 0
#         for i in grid:
#             for j in i:
#                 if j < 0:
#                     count += 1
#         return count

# second solution
# time: O(n+m)
# space: O(n)

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         merge_arr = []
#         for g in grid:
#             merge_arr.extend(g)
#         count = 0
#         for n in merge_arr:
#             if n < 0:
#                 count += 1
#         return count

# third solution
# time: O(nlogn)
# space: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for g in grid:
            left,right = 0, len(g)-1
            while left <= right:
                mid = (left + right) // 2
                if g[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += len(g) - left
        return count


s = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(s.countNegatives(grid))