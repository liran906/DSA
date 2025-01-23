# Top K Frequent Elements
# https://neetcode.io/problems/top-k-elements-in-list
# med

class Solution:
    def topKFrequent(self, nums, k):
        hashtable = {}
        for i in nums:
            hashtable[i] = hashtable.get(i, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in hashtable.items():
            bucket[freq].append(num)
        result = []
        counter = 0
        for nums in bucket[::-1]:
            for num in nums:
                result.append(num)
                counter += 1
                if counter == k:
                    return result