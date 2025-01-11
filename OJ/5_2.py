# counter = 0
# def hanoi_4p(n, a, b, c, d):
#     global counter
#     if n == 1:
#         counter += 1
#         print(a,'->',d)
#     elif n == 2:
#         counter += 3
#         print(a,'->',b)
#         print(a,'->',d)
#         print(b,'->',d)
#     else:
#         hanoi_4p(n - 2, a, c, d, b) # n-2, a->b
#         print(a,'->',c) # n-1, a->c
#         print(a,'->',d) # n, a->d
#         print(c,'->',d) # n-1, c->d
#         hanoi_4p(n - 2, b, a, c, d) # n-2, b->d
#         counter += 3
#     return counter

# print(hanoi_4p(4,'a','b','c','d'))

# 上面是方便理解，现在按照 oj 要求：
# counter = 0
# def hanoi_4p(n):
#     global counter
#     if n == 1:
#         counter += 1
#     elif n == 2:
#         counter += 3
#     else:
#         hanoi_4p(n - 2)
#         counter += 3
#         hanoi_4p(n - 2)
#     return counter

# n = int(input())
# print(hanoi_4p(n))

# 本想优化一下算法复杂度，结果更差：
# counter = 0
# def hanoi_4p(n):
#     global counter
#     if n == 1:
#         counter += 1
#         return counter
#     elif n == 2:
#         counter += 3
#         return counter
#     elif n == 3:
#         counter += 5
#         return counter
#     else:
#         hanoi_4p(n - 3)
#         counter += 5
#         hanoi_4p(n - 3)
#         hanoi_4p(n - 3)
#         hanoi_4p(n - 3)
#     return counter

# n = int(input())
# print(hanoi_4p(n))

# ---------------------------------
n = 20
cache = [None] * (n + 1)

def hanoi_4p_2(n):
    if cache[n]:
        return cache[n]
    if n == 0:
        cache[n] = 0
    elif n == 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 3
    else:
        h = []
        for i in range(1, n):
            h.append(hanoi_4p_2(i) * 2 + 2 ** (n - i) - 1)
        cache[n] = min(h)
    return cache[n]

from functools import lru_cache

@lru_cache(maxsize=5120)
def hanoi_4p(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        h = []
        for i in range(1, n):
            h.append(hanoi_4p(i) * 2 + 2 ** (n - i) - 1)
        return min(h)


print(hanoi_4p_2(n))

print(hanoi_4p(n))