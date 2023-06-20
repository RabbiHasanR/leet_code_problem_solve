class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = {}

        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        values = list(hash_map.values())
        return all(value == values[0] for value in values)