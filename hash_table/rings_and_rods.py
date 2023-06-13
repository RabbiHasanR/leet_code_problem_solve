from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        result = defaultdict(list)
        count = 0
        for i in range(0, len(rings), 2):
            color = rings[i:i+2]
            result[color[1]].append(color[0])
        for value in result.values():
            if 'B' in value and 'G' in value and 'R' in value:
                count += 1
        return count