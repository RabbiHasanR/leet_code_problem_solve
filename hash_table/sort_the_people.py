from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result_dict = {}
        for i in range(len(names)):
            result_dict[heights[i]] = names[i]
        keys = sorted(result_dict.keys(), reverse=True)
        return [result_dict[key] for key in keys]