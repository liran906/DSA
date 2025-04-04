class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        nxt = self.getNext(needle)
        i = j = 0
        while j < len(haystack):
            while j < len(haystack) and i < len(needle) and needle[i] == haystack[j]:
                i += 1
                j += 1
            if i == len(needle):
                return j - i
            if i > 0:
                i = nxt[i-1]
            else:
                j += 1
        return -1
    
    def getNext(self, pstr):
        i = 0
        nxt = [0] * len(pstr)
        for j in range(1, len(pstr)):
            while pstr[i] != pstr[j] and i > 0:
                i = nxt[i-1]
            if pstr[i] == pstr[j]:
                i += 1
            nxt[j] = i
        return nxt

s = Solution()
print(s.strStr('abc','c'))