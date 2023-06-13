from typing import List
from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_map = defaultdict(list)
        key = 0
        for num in nums:
            if key in hash_map:
                if num not in hash_map[key]:
                    hash_map[key].append(num)
                else:
                    count = 0
                    for i, item in hash_map.items():
                        if num not in item:
                            hash_map[i].append(num)
                            count = 1
                            break

                    if count == 0:
                        key += 1
                        hash_map[key].append(num)
            else:
                hash_map[key].append(num)
        return list(hash_map.values())
        