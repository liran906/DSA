# Kth Largest Element in an Array
# https://neetcode.io/problems/kth-largest-element-in-an-array
# m

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        minheap = []
        for i in nums:
            heapq.heappush(minheap, i)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return heapq.heappop(minheap)

# Using quick select method. average case O(n), worst case O(n^2)
class Solution:
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, len(nums) - k, 0, len(nums) - 1)

    def quickSelect(self, arr, k, l, r):
        pivot = arr[r]
        pointer = l
        for i in range(l, r):
            if arr[i] <= pivot:
                arr[pointer], arr[i] = arr[i], arr[pointer]
                pointer += 1
        arr[pointer], arr[r] = arr[r], arr[pointer]

        if pointer == k:
            return arr[pointer]
        elif pointer < k:
            return self.quickSelect(arr, k, pointer + 1, r)
        else:
            return self.quickSelect(arr, k, l, pointer - 1)

s = Solution()
print(s.findKthLargest([3,5,1,2,8], 5))