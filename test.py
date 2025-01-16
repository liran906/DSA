from collections import deque

def flood_fill(maze, region, start_row, start_col, region_id):
    """标记连通区域编号"""
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start_row, start_col)])
    notation = maze[start_row][start_col]
    
    while queue:
        x, y = queue.popleft()
        if region[x][y] != -1:  # 已经标记过
            continue
        region[x][y] = region_id  # 标记当前点
        
        # 遍历四个方向
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and region[nx][ny] == -1 and maze[nx][ny] == notation:
                queue.append((nx, ny))

# 输入处理
rows, cols = map(int, input().split())
maze = [list(input().strip()) for _ in range(rows)]
location_num = int(input())
locations = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(location_num)]

# 预处理：标记每个连通区域
region = [[-1] * cols for _ in range(rows)]  # 初始化区域编号矩阵
current_region_id = 0

for r in range(rows):
    for c in range(cols):
        if region[r][c] == -1:  # 未被标记
            flood_fill(maze, region, r, c, current_region_id)
            current_region_id += 1

# 处理每个查询
for start_row, start_col, end_row, end_col in locations:
    if region[start_row][start_col] != region[end_row][end_col]:
        print("neither")
    else:
        if maze[start_row][start_col] == '1':
            print("decimal")
        else:
            print("binary")