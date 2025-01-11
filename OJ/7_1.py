def pivottest(inp):
    l = [int(i) for i in inp.split()]
    out = []
    for i in range(len(l)):
        left = l[:i]
        right = l[i+1:]
        done = True
        for j in left:
            if j > l[i]:
                done = False
                break
        if done:
            for k in right:
                if k < l[i]:
                    done = False
                    break
        if done:
            out.append(str(l[i]))
    return len(out), ' '.join(out)

string = input()
n, item = pivottest(string)
print(n)
print(item)