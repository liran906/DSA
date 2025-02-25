# Number of Islands
# https://neetcode.io/problems/count-number-of-islands
# m

# using the flood-fill algorithm inspired by the 10 kinds of people problem.
class Solution:
    def numIslands(self, grid):
        region = [[0 for _ in sublist] for sublist in grid]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        region_id = 1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # if not marked and is land
                if not region[r][c] and grid[r][c] == '1':
                    queue = [[r, c]]
                    # dfs (bfs the same)
                    while queue:
                        cr, cc = queue.pop() # current_row & current_column
                        if not region[cr][cc] and grid[cr][cc] == grid[r][c]:
                            # mark the region
                            region[cr][cc] = region_id

                            # add new [r, c] to queue.
                            for _r, _c in directions:
                                nr, nc = cr + _r, cc + _c
                                if nr >= 0 and nr < len(grid) and nc >= 0 and nc <len(grid[r]) and not region[nr][nc]:
                                    queue.append([nr, nc])
                    region_id += 1 # after one search round, id plus 1
        # minus 1 because after the last search, an extra 1 was added to id.
        return region_id - 1

# without the region marking
# just mark the land as 0 after searched instead
# save some space
class Solution:
    def numIslands(self, grid):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # if is land
                if grid[r][c] == '1':
                    stack = [[r, c]]
                    # dfs (bfs the same)
                    while stack:
                        cr, cc = stack.pop() # current_row & current_column
                        if grid[cr][cc] == '1':
                            # mark the as 0
                            grid[cr][cc] = '0'

                            # add new [r, c] to stack.
                            for _r, _c in directions:
                                nr, nc = cr + _r, cc + _c
                                if nr >= 0 and nr < len(grid) and nc >= 0 and nc <len(grid[r]) and grid[nr][nc] == '1':
                                    stack.append([nr, nc])
                    count += 1 # after one search round, id plus 1
        return count