# https://kamacoder.com/problempage.php?pid=1044

import sys

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    n, m = data[0], data[1]
    data = data[2:]
    # 分别为水平行之和的 list 和垂直列之和的 list
    horizonal = [0] * n
    veritical = [0] * m
    i = 0
    
    while i < len(data):
        veritical[i % m] += data[i]
        horizonal[i // m] += data[i]
        i += 1

    hsum = [0]
    for i in range(n): # horizonal
        hsum.append(horizonal[i] + hsum[-1])
    vsum = [0]
    for i in range(m): # vertical
        vsum.append(veritical[i] + vsum[-1])

    # 前缀和 比较:最后一项减当前项 与 当前项
    # 最小的差值即为结果
    res = float('inf')
    for i in hsum:
        res = min(res, abs((hsum[-1] - i) - i))
    for i in vsum:
        res = min(res, abs((vsum[-1] - i) - i))
    return res

print(main())