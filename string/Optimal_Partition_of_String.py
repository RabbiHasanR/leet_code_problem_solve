from collections import defaultdict

class Solution:
    def partitionString(self, s: str) -> int:

        hash_map = defaultdict(list)
        key = 0

        for c in s:
            if key in hash_map:
                if c not in hash_map[key]:
                    hash_map[key].append(c)
                else:
                    key += 1
                    hash_map[key].append(c)
            else:
                hash_map[key].append(c)
        return len(hash_map.values())