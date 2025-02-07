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

# Using quick select method. Same as 036.
class Solution:
    def kClosest(self, points, k):
        if k == len(points):
            return points

        def quickSelect(l, r):
            pivot = points[r][0] ** 2 + points[r][1] ** 2
            pointer = l
            for i in range(l, r):
                if points[i][0] ** 2 + points[i][1] ** 2 <= pivot:
                    points[i], points[pointer] = points[pointer], points[i]
                    pointer += 1
            
            points[r], points[pointer] = points[pointer], points[r]
            if pointer > k:
                return quickSelect(l, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, r)
            else:
                return points[:pointer] # not pointer + 1, because pointer starts from 0, while k starts from 1
        
        return quickSelect(0, len(points) - 1)