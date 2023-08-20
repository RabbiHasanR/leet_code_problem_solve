class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0
        s_index = 0
        
        if s == '':
            return True

        while t_index < len(t):
            if s_index < len(s) and s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
            else:
                t_index += 1
        return s_index == len(s)