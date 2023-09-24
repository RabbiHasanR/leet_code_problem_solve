from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        hash_map_A = {}
        hash_map_temp = {}
        for item in range(len(A)):
            hash_map_A[A[item]] = item
        for i in range(len(B)):
            count = 0
            hash_map_temp[B[i]] = i
            for key, value in hash_map_temp.items():
                if key in hash_map_A and hash_map_A[key] <= i:
                    count += 1
            result.append(count)
                
        return result
        