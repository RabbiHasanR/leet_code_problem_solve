from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        hash_map = {}
        count = 0
        for word in words:
            reverse_word = word[::-1]
            if reverse_word in hash_map:
                count += 1
            hash_map[word] = reverse_word
        return count