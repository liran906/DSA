# char = '00'
# input = 27
# output = [[char for _ in range(input)] for _ in range(input)]

# def ssquare(n, x=0, y=0):
#     num = len(char)
#     space = ' ' * num
#     n_unit = int(n / 3)
#     for i in range(n_unit + x, 2 * n_unit + x):
#         for j in range (n_unit + y, 2 * n_unit + y):
#             output[i][j] = space
#     if n > 3:
#         for x in range(0, n, n_unit):
#             for y in range(0, n, n_unit):
#                 ssquare(n_unit, x, y)

# def ssquare(input, x=0, y=0):
#     n = int(input / 3)
#     space = ' ' * len(char)
#     for i in range(n * (1 + 3 * x), n * (2 + 3 * x)):
#         for j in range(n * (1 + 3 * y), n * (2 + 3 * y)):
#             output[i][j] = space
#     if n >= 3:
#         for x in [0, 1, 2]:
#             for y in [0, 1, 2]:
#                 ssquare(n, x, y)

# ssquare(input)
# for i in output:
#     print(''.join(i))

# 这次很遗憾，没有考虑上一级的偏移量
# char = '00'
# lenth = 27
# space = ' ' * len(char)
# output = [[char for _ in range(lenth)] for _ in range(lenth)]

# def ssquare(lenth, x=0, y=0): # lenth >= 3
#     unit = int(lenth / 3)
#     mid = lenth // 2
#     offset = unit // 2
#     for i in range(mid - offset, mid + offset + 1):
#         for j in range(mid - offset, mid + offset + 1):
#             output[i+x][j+y] = space
#     if lenth >= 3:
#         for x in [0, unit, 2*unit]:
#             for y in [0, unit, 2*unit]:
#                 ssquare(unit, x, y)

# ssquare(lenth)
# for i in output:
#     print(''.join(i))

char = '00'
lenth = 27
space = ' ' * len(char)
output = [[char for _ in range(lenth)] for _ in range(lenth)]

def ssquare(lenth, x=0, y=0):  # x y 是左上角坐标
    unit = lenth // 3
    # 填充中心空白块
    xstart, ystart = x + unit, y + unit
    xstop, ystop = xstart + unit, ystart + unit
    for i in range(xstart, xstop):
        for j in range(ystart, ystop):
            output[i][j] = space
    # 对剩余的 8 个子块递归调用
    if unit >= 3:
        for dx in [0, unit, 2 * unit]:
            for dy in [0, unit, 2 * unit]:
                if dx == unit and dy == unit:
                    continue  # 跳过中心块
                # 这里注意！是上一轮偏移量 x 加上本轮偏移量 dx
                ssquare(unit, x + dx, y + dy)

# 调用递归函数并打印结果
ssquare(lenth)
for line in output:
    print(''.join(line))