# 递归方法
total = 30
tilelen = [1,2,3,4]
cache = [None] * (total + 1)

def tile(totallen, currentlen=0):
    if currentlen > totallen:
        return 0
    if cache[currentlen] is not None:
        return cache[currentlen]
    if currentlen == totallen:
        return 1

    count = 0 # 不需要全局变量。因为每一层递归函数的参数都是独立的，而且函数最后也返回了 count，所以子函数的 count 会自动累加到主函数的 count 中。
    for l in tilelen:
        # currentlen += l # ！不能再循环中直接改。不然影响下一次循环
        count += tile(totallen, currentlen + l)
    cache[currentlen] = count
    return count

print(tile(total))

# 动态规划方法
def tile_2(totallen):
    for lenth in range(totallen + 1):
        if lenth == 0:
            cache[lenth] = 1
            continue
        else:
            count = 0
            for tlenth in [l for l in tilelen if l <= lenth]:
                count += cache[lenth - tlenth]
            cache[lenth] = count
    return cache[totallen]

print(tile_2(total))

# 递归方法-按课程
cache = {}

def tile_3(lenth):
    if lenth in cache:
        return cache[lenth]
    if lenth == 1 or lenth == 0:
        cache[lenth] = 1
        return 1
    else:
        count = 0
        for l in [_ for _ in tilelen if _ <= lenth]:
            count += tile_3(lenth - l)
        cache[lenth] = count
        return count

print(tile_3(total))

# 递归方法2-按课程
cache = {1:1, 0:1, -1:0, -2:0, -3:0} # 提前写入 -3 ～ 1的情况，就不用再用 if 判断了

def tile_3(lenth):
    if lenth in cache:
        return cache[lenth]
    result = (tile_3(lenth - 1) + tile_3(lenth - 2) + tile_3(lenth - 3) + tile_3(lenth - 4))
    cache[lenth] = result
    return result

print(tile_3(total))

# 动态规划-按课程
cache = {1:1, 0:1, -1:0, -2:0, -3:0} # 提前写入 -3 ～ 1的情况，就不用再用 if 判断了

def tile_4(lenth):
    if lenth in cache:
        return cache[lenth]
    for l in range(2, lenth + 1):
        cache[l] = cache[l-1] + cache[l-2] + cache[l-3] + cache[l-4]
    return cache[lenth]

print(tile_4(total))