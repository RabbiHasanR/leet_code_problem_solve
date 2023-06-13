from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result_dict = defaultdict(list)
        results = []
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size in result_dict:
                result_dict[size].append(i)
            else:
                result_dict[size].append(i)

        for key, item in result_dict.items():
            if len(item) > key:
                for i in range(0, len(item), key):
                    results.append(item[i:i+key])
            else:
                results.append(item)
        
        return results