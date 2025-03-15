# https://leetcode.cn/problems/spiral-matrix-ii/
# m

class Solution(object):
    def generateMatrix(self, n):
        mat = [[0 for i in range(n)] for i in range(n)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        i = 1
        r, c = 0, 0
        rem = 0
        while i <= n ** 2:
            while 0 <= r < n and 0 <= c < n and mat[r][c] == 0:
                mat[r][c] = i
                i += 1
                r, c = r + directions[rem][0], c + directions[rem][1]
            r, c = r - directions[rem][0], c - directions[rem][1]
            rem = (rem + 1) % 4
            r, c = r + directions[rem][0], c + directions[rem][1]
        return mat

# 稍微改进了点写法
class Solution(object):
    def generateMatrix(self, n):
        mat = [[0 for i in range(n)] for i in range(n)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        i = 1
        r, c = 0, 0
        rem = 0
        while i <= n ** 2:
            while 0 <= r < n and 0 <= c < n and mat[r][c] == 0:
                mat[r][c] = i
                i += 1
                nr, nc = r + directions[rem][0], c + directions[rem][1]
                if 0 <= nr < n and 0 <= nc < n and mat[nr][nc] == 0:
                    r, c = nr, nc
            rem = (rem + 1) % 4
            r, c = r + directions[rem][0], c + directions[rem][1]
        return mat

# 少了个 while，但本质还是和上面一样的
class Solution(object):
    def generateMatrix(self, n):
        mat = [[0 for i in range(n)] for i in range(n)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        i = 1
        r, c = 0, 0
        rem = 0
        while i <= n ** 2:
            mat[r][c] = i
            i += 1
            nr, nc = r + directions[rem][0], c + directions[rem][1]
            if 0 <= nr < n and 0 <= nc < n and mat[nr][nc] == 0:
                r, c = nr, nc
            else:
                rem = (rem + 1) % 4
                r, c = r + directions[rem][0], c + directions[rem][1]
        return mat

s = Solution()
print(s.generateMatrix(5))