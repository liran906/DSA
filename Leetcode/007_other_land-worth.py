import sys

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    n, m = data[0:1]
    matrix = []
    data = data[2:]
    for r in range(n):
        matrix.append([i for i in data[:m]])
        data = data[m:]
    horizonal = [0] * m
    for i in range(n):
        horizonal[i] = sum(matrix[i])

    veritical = [0] * n
    for i in range(m):
        veritical[i] = sum()

    for r in range(n):
        veritical[r] = 0
        for c in range(m):
            veritical[r] += data[n * m]