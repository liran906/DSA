# Valid Parentheses
# https://neetcode.io/problems/validate-parentheses
# easy

class Solution:
    def isValid(self, s):
        stack = []
        d = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in d:
                stack.append(c)
            elif c in d.values():
                if stack == [] or d[stack.pop()] != c:
                    return False
        return stack == []