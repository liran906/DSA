# K Closest Points to Origin
# https://neetcode.io/problems/k-closest-points-to-origin
# m

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for i in points:
            dis = i[0]**2 + i[1]**2
            heapq.heappush(maxheap, (-dis, i))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        res = []
        while maxheap:
            res.append(heapq.heappop(maxheap)[1])
        return res