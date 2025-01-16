from collections import deque

q = deque('abcdef')
print(q)
p = q.popleft()
print(p, type(p))
print(q, type(q))
q.append('g')
print(q)
q.append('hij')
print(q)

q2 = deque('hij')
q += q2
print(q)
print(len(q))