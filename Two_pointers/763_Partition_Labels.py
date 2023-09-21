from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        end = 0
        index = 0
        result = []
        hash_map = {}

        for c in range(len(s)):
            hash_map[s[c]] = c
        
        while index < len(s):
            end = max(end, hash_map[s[index]])
            if index == end:
                result.append(end - start + 1)
                start = end + 1
            index += 1
        return result