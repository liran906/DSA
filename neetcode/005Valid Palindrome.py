# Valid Palindrome
# https://neetcode.io/problems/is-palindrome
# easy

# class Solution:
#     def isPalindrome(self, s):
#         pword = ''
#         s = s.lower()
#         for char in s:
#             if char in 'abcdefghijklmnpoqrstuvwxyz':
#                 pword += char
#         return pword == pword[::-1]

class Solution:
    def isPalindrome(self, s):
        pword = ''
        for char in s:
            if char.isalnum(): # numbers as well as alphabits
                pword += char.lower()
        return pword == pword[::-1]

sol = Solution()
print(sol.isPalindrome("0P"))