def firstBad(start, end):
    if end < start: # 相等的时候还要再判断一次才行
        return start

    else:
        mid = (start + end) // 2
        if isbad(mid):
            return firstBad(start, mid - 1)
        else:
            return firstBad(mid + 1, end)

n = int(input())
isbad = eval(input())
print(firstBad(1,n))