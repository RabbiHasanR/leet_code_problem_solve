from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for items in image:
            left = 0
            right = len(items) - 1

            while left <= right:
                temp = items[left]
                items[left] = 1 if items[right] == 0 else 0
                items[right] = 1 if temp == 0 else 0
                left += 1
                right -= 1
                
        return image