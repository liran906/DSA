def func(S):
    current = S
    output = S
    for _ in range(len(S)):
        front = current[0]
        current = current[1:] + front
        if current < output:
            output = current
    return output

S = eval(input())
print(func(S))