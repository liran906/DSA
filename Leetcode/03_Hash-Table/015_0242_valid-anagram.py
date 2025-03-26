# https://leetcode.cn/problems/valid-anagram/
# e

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        htable = dict()
        for i in s:
            htable[i] = htable.get(i, 0) + 1
        
        for i in t:
            if i not in htable:
                return False
            htable[i] -= 1
        
        for i in htable.values():
            if i: # not 0
                return False
        return True
    
# go
# func isAnagram(s string, t string) bool {
#     if len(s) != len(t) {
#         return false
#     }
#     var ch [26]int
    
#     for _, c := range s {
#         ch[c - 'a']++
#     }
#     for _, c := range t {
#         ch[c - 'a']--
#         if ch[c - 'a'] < 0 {
#             return false
#         }
#     }
#     for _, c := range ch {
#         if c != 0 {
#             return false
#         }
#     }
#     return true
# }