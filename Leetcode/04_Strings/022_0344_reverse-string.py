class Solution(object):
    def reverseString(self, s):
        l, r = 0, len(s)-1
        while l < r:
            s[r], s[l] = s[l], s[r]
            r -= 1
            l += 1

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        注意当 [:] 在左侧时，不是表达切片浅拷贝全部，而是原地修改的意思
        """
        s[:] = reversed(s)
        print(s)


a = [1,2,[3,4]]
b = a[:]

b[0] = 9
print(a) # [1, 2, [3, 4]]

b[2][0] = 9
print(a) # [1, 2, [9, 4]]