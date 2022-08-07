# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# first solution
# time O(nlogn)
# space O(1)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         return False


# second solution
# time O(n)
# space O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countOne = [0] * 26
        countTwo = [0] * 26
        for c in s:
            countOne[ord(c) - ord('a')] +=1
        for c in t:
            countTwo[ord(c) - ord('a')] +=1
            
        if countOne == countTwo:
            return True
        return False
        

sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))