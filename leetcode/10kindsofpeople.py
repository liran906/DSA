# https://open.kattis.com/problems/10kindsofpeople

# def move(notation, maze, visitlist, start_row, start_col, end_row, end_col):
#     if start_row < 0 or start_row >= len(maze) or start_col < 0 or start_col >= len(maze[0]):
#         return False
#     elif maze[start_row][start_col] != notation:
#         return False
#     elif visitlist[start_row][start_col]:
#         return False
#     elif start_row == end_row and start_col == end_col:
#         return True
#     else:
#         # mark the current position as searched
#         visitlist[start_row][start_col] = True
#         # find in four directions
#         found = move(notation, maze, visitlist, start_row + 1, start_col, end_row, end_col) or \
#         move(notation, maze, visitlist, start_row - 1, start_col, end_row, end_col) or \
#         move(notation, maze, visitlist, start_row, start_col + 1, end_row, end_col) or \
#         move(notation, maze, visitlist, start_row, start_col - 1, end_row, end_col)
#         return found

# # start reading the input
# rows, collums = list(map(int, input().split()))
# mazelist = []
# for _ in range(rows):
#     mazelist.append([t for t in input()])
# location_num = int(input())
# location = []
# for _ in range(location_num):
#     location.append(list(map(lambda x: int(x)-1, input().split()))) # need to -1 cause not starting from 0
# # finished reading the input

# # start searching the maze
# for i in location:
#     start_row, start_col, end_row, end_col = i
#     visitlist = [[False]*collums for _ in range(rows)]
#     if mazelist[start_row][start_col] != mazelist[end_row][end_col]:
#         print('neither')
#     else:
#         notation = mazelist[start_row][start_col]
#         result = move(notation, mazelist, visitlist, start_row, start_col, end_row, end_col)
#         if result:
#             if notation == '1':
#                 print('decimal')
#             else:
#                 print('binary')
#         else:
#             print('neither')

'''
The algorithm above is TOTALLY ABLE TO SOLVE THE QUESTION, however upon subbmission, the 23rd test case won't pass, 
with 'runtime error' indicated. I think it's because of exceeding max recrusion depth, or multiple calculations
on the same maze (because of multiple start & end location sets).
Given this, with the help of gpt, came up with this new algorithm below: flood-fill.
it calculates the maze once, and returns the expected result base on that.
'''

from collections import deque

def flood_fill(maze, region, region_id, r, c, notation):
    searchQ = deque([(r,c)])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while len(searchQ) > 0:
        r, c = searchQ.popleft()
        if region[r][c]:
            continue
        region[r][c] = region_id
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr >= 0 and nr < len(region) and nc >= 0 and nc < len(region[0]):
                if not region[nr][nc] and maze[nr][nc] == notation:
                    searchQ.append((nr, nc))
    return region

# start reading the input
rows, collums = map(int, input().split())
mazelist = [[t for t in input()] for _ in range(rows)]
location_num = int(input())
locations = [list(map(lambda x: int(x)-1, input().split())) for _ in range(location_num)]

# start marking the maze regions
region = [[0]*collums for _ in range(rows)]
region_id = 1
for row in range(rows):
    for col in range(collums):
        if not region[row][col]: # has not been marked yet
            notation = mazelist[row][col]
            region = flood_fill(mazelist, region, region_id, row, col, notation)
            region_id += 1

# address each location
for start_row, start_col, end_row, end_col in locations:
    if region[start_row][start_col] == region[end_row][end_col]:
        if mazelist[start_row][start_col] == '1':
            print('decimal')
        else:
            print('binary')
    else:
        print('neither')