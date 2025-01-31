# Plus One
# https://neetcode.io/problems/plus-one
# e

class Solution:
    def plusOne(self, digits):
        return [i for i in str(int(''.join([str(i) for i in digits])) + 1)]