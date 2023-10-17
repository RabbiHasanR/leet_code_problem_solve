from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squres = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squres[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squres[(r // 3, c // 3)].add(board[r][c])
        return True
