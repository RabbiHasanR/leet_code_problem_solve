from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        small = skill[0]
        large = skill[len(skill) - 1]
        target = small + large

        left = 0
        right = len(skill) - 1
        result = 0

        while left < right:
            if target == (skill[left] + skill[right]):
                result += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
        return result


        