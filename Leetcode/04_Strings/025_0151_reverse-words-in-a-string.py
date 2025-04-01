class Solution(object):
    def reverseWords(self, s):
        sp = s.split()
        l, r = 0, len(sp) - 1
        while l < r:
            sp[l], sp[r] = sp[r], sp[l]
            l += 1
            r -= 1
        return ' '.join(sp)

class Solution(object):
    def reverseWords(self, s):
        words = []
        i = 0
        while i < len(s):
            word = ''
            while i < len(s) and s[i] != ' ':
                word += s[i]
                i += 1
            if word:
                words.append(word)
            i += 1
        
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return ' '.join(words)