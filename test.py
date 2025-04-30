def minstep(n):
    if n == 1:
        return 0
    step = minstep(n-1)
    if n % 2 == 0:
        step = min(step, minstep(n//2))
    if n % 3 == 0:
        step = min(step, minstep(n//3))
    return step + 1

print(minstep(24))