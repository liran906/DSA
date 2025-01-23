# Encode and Decode Strings
# https://neetcode.io/problems/string-encode-and-decode
# med

class Solution:
    def __init__(self):
        self.keypool = '!@#$%^&*()<>?:"{},./;|\+=_-[]'
        self.index = 0

    def encode(self, strs):
        if strs == ['']:
            return ''
        if strs == []:
            return 'None'
        for i in strs:
            while self.keypool[self.index] in i:
                self.index += 1
        return self.keypool[self.index].join(strs)

    def decode(self, s):
        if s == 'None':
            return []
        if s == '':
            return ['']
        return s.split(self.keypool[self.index])