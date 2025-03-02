# Islands and Treasure
# https://neetcode.io/problems/islands-and-treasure
# m

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue = deque()
                    queue.append((r, c))
                    d = 1
                    reached = set()
                    outer_count, inner_count = 1, 0 # to store the number of nodes on one depth.
                    while queue:
                        ir, ic = queue.popleft()
                        outer_count -= 1
                        reached.add((ir, ic))
                        
                        for dr, dc in directions:
                            cr, cc = ir + dr, ic + dc
                            if cr >= 0 and cr < rows and cc >= 0 and cc < cols and grid[cr][cc] > 0 and \
                            (cr, cc) not in reached and (cr, cc) not in queue:
                                inner_count += 1
                                grid[cr][cc] = min(d, grid[cr][cc])
                                queue.append((cr, cc))

                        if outer_count == 0:
                            d += 1
                            outer_count = inner_count
                            inner_count = 0

s = Solution()
grid = [
  [9,-1,0, 9],
  [9, 9,9,-1],
  [9,-1,9,-1],
  [0,-1,9, 9]
]
s.islandsAndTreasure(grid)
print(grid)