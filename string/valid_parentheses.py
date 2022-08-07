# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false



class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s)%2 == 1:
            return False
        stack = []
        
        for c in s:
            if c == ')':
                if len(stack) == 0 or stack.pop(len(stack)-1) != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop(len(stack)-1) != '{':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop(len(stack)-1) != '[':
                    return False
            else:
                stack.append(c)
        if len(stack) > 0:
            return False
        return True


s = "()"

solution = Solution()
print(solution.isValid(s))
        