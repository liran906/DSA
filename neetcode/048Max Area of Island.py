# Max Area of Island
# https://neetcode.io/problems/max-area-of-island
# m

# same as 047.
class Solution:
    def maxAreaOfIsland(self, grid):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        max_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    stack = [(r,c)]
                    count = 0
                    # dfs
                    while stack:
                        cr, cc = stack.pop()
                        if grid[cr][cc]:
                            count += 1
                            grid[cr][cc] = 0
                            for _r, _c in directions:
                                nr, nc = cr + _r, cc + _c
                                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc]:
                                    stack.append((nr,nc))
                    max_count = max(max_count, count)
        return max_count