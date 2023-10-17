from collections import defaultdict
from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        rows = defaultdict(set)
        cols = defaultdict(set)

        if row != col:
            return False

        for r in range(row):
            for c in range(col):
                if matrix[r][c] not in rows[r]:
                    rows[r].add(matrix[r][c])
                if matrix[r][c] not in cols[c]:
                    cols[c].add(matrix[r][c])
        for r in rows:
            if len(rows[r]) != row:
                return False
        for c in cols:
            if len(cols[c]) != col:
                return False
        
        return True
        