# https://open.kattis.com/problems/2048
# 2.7

def rotatelst(lst):
    # clockwise rotation
    r_lst = [[] for i in range(4)]
    for j in reversed(range(4)):
        for i in range(4):
            r_lst[3-j].append(lst[i][j])
    return r_lst

def next_2048(o_lst, dir):
    # 旋转到相当于向左移
    for i in range(dir):
        o_lst = rotatelst(o_lst)

    # 向左移
    n_lst = [[] for i in range(4)]
    for i in range(4):
        n_lst[i] = [num for num in o_lst[i] if num != 0]
        j = 0
        while len(n_lst[i]) > 1 and j < len(n_lst[i]) - 1: # 判断是否归并
            if n_lst[i][j] == n_lst[i][j+1]:
                n_lst[i][j] *= 2
                n_lst[i].pop(j+1)
            j += 1
        while  len(n_lst[i]) < 4:
            n_lst[i].append(0)
    
    # 继续转回原方向
    if dir > 0:
        for i in range(4 - dir):
            n_lst = rotatelst(n_lst)
    return n_lst

in_lst = [[] for i in range(4)]

for i in range(4):
    in_lst[i] = list(map(int, input().split()))
direction = int(input())

result_lst = next_2048(in_lst, direction)
for i in result_lst:
    print(' '.join(list(map(str, i))))