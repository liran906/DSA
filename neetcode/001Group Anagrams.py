# Group Anagrams
# https://neetcode.io/problems/anagram-groups
# med

class Solution:
    def groupAnagrams(self, strs):
        bucket = []
        for word in strs:
            alph = {}
            for char in word:
                alph[char] = alph.get(char, 0) + 1
            bucket.append(alph)
        
        result = []
        allocated = []
        for i in range(len(strs)):
            if i in allocated:
                continue
            result.append([strs[i]])
            for j in range(i+1, len(strs)):
                if j in allocated:
                    continue
                if bucket[i] == bucket[j]:
                    result[-1].append(strs[j])
                    allocated.append(j)
        
        return result