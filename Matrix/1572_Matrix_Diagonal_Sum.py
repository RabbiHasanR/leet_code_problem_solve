from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        result = 0
        row = len(mat)
        col = len(mat[0])

        for r in range(row):
            for c in range(col):
                if r == c or r == (row - c - 1):
                    result += mat[r][c]
        return result