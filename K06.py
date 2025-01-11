# 单词最小编辑距离的递归解法(不放操作列表)
cache = {}

def reWordEdit(original, target, oplist):
    score = 0

    # 检查缓存
    if (original, target) in cache:
        return cache[(original, target)]

    # 边界条件：直接返回结果
    if original == '' and target == '':
        return 0
    if original == '':
        # 剩余所有字符都需要插入
        score = len(target) * oplist['insert']
        cache[(original, target)] = score
        return score
    if target == '':
        # 剩余所有字符都需要删除
        score = len(original) * oplist['delete']
        cache[(original, target)] = score
        return score

    # 获取当前字符
    o, t = original[-1], target[-1]

    # 递归计算（不放 operation 主要为了这里简洁一点）
    if o == t:
        score = min(
            reWordEdit(original[:-1], target, oplist) + oplist['delete'],
            reWordEdit(original, target[:-1], oplist) + oplist['insert'],
            reWordEdit(original[:-1], target[:-1], oplist) + oplist['copy']
        )
    else:
        score = min(
            reWordEdit(original[:-1], target, oplist) + oplist['delete'],
            reWordEdit(original, target[:-1], oplist) + oplist['insert']
        )

    # 缓存结果
    cache[(original, target)] = score
    return score

# 加入 operations
def reWordEdit(original, target, oplist):
    score = 0
    operations = []

    # 如果已经在 cache 中，直接返回
    if (original, target) in cache:
        return cache[(original, target)]

    # 如果两个字符串都为空，返回初始状态
    if original == '' and target == '':
        return 0, []  # 分数为0，操作序列为空

    # 如果其中一个为空
    if original == '':
        score = len(target) * oplist['insert']
        operations = ['insert ' + c for c in target]
        cache[(original, target)] = (score, operations)
        return score, operations

    if target == '':
        score = len(original) * oplist['delete']
        operations = ['delete ' + c for c in original]
        cache[(original, target)] = (score, operations)
        return score, operations

    # 获取当前字符
    o, t = original[-1], target[-1]

    # 分情况讨论
    if o == t:  # 当前字符相等
        score_copy, ops_copy = reWordEdit(original[:-1], target[:-1], oplist)
        score_copy += oplist['copy']
        ops_copy = ops_copy + ['copy ' + o] # 这里不能用 += 余同。因为不是创建新表了
    else:  # 当前字符不相等
        score_copy = float('inf')
        ops_copy = []

    # 删除操作
    score_delete, ops_delete = reWordEdit(original[:-1], target, oplist)
    score_delete += oplist['delete']
    ops_delete = ops_delete + ['delete ' + o]

    # 插入操作
    score_insert, ops_insert = reWordEdit(original, target[:-1], oplist)
    score_insert += oplist['insert']
    ops_insert = ops_insert + ['insert ' + t]

    # 选择最小的分数路径
    if score_copy <= score_delete and score_copy <= score_insert:
        result = (score_copy, ops_copy)
    elif score_delete <= score_insert:
        result = (score_delete, ops_delete)
    else:
        result = (score_insert, ops_insert)

    # 缓存结果
    cache[(original, target)] = result
    return result


print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy': 5, 'delete': 10, 'insert': 15}
originalWords = [
    "cane", "sheep", "algorithm", "debug", "difficult", "directory",
    "wonderful"
]
targetWords = [
    "new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"
]
for i in range(len(originalWords)):
    score, operations = reWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)