# Description:
# Design a algorithm to encode and decode a string. The encoded string is 
# then sent over the network and is decoded back to the original list of strings.
# plese implement ecode and decode

# Example 1:
# Input: ["a","b","c","d"]
# Output: ["a","b","c","d"]

# Explanation: 
# one possible ecode method is : "a:;b:;c:;d:;"

# first solution
# time: O(n)
# space: O(1)


class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            j = i

            while j < len(str) and str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = j+1+length
        return res

sol = Solution()
strs = ["lint","code","love", "you"]
decodeStr = sol.encode(strs)
print(decodeStr)
print(sol.decode(decodeStr))
