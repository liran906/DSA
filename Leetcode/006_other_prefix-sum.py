# https://kamacoder.com/problempage.php

# 普通方法 O(n*t)
def sums(nums, s, e):
    res = 0
    while s <= e:
        res += nums[s]
        s += 1
    return res

import sys

data = list(map(int, sys.stdin.read().strip().split()))

n = data[0]
nums = data[1:n+1]

index = n + 1
while index < len(data):
    print(sums(nums, data[index], data[index+1]))
    index += 2


# 前缀和 O(1*t)
# 累加前 n 个数，sum(3,5) = sum(5) - sum(2)
import sys

def prefix_sum():
    data = list(map(int, sys.stdin.read().strip().split()))

    n = data[0]
    nums = [0] * (n + 1) # 需要多创建一个 和为0的情况(第一个值)
    for i in range(1, n + 1):
        nums[i] = data[i] + nums[i-1]

    idx = n + 1
    while idx < len(data):
        srt = data[idx]
        end = data[idx+1]
        print(nums[end+1] - nums[srt])
        idx += 2

prefix_sum()