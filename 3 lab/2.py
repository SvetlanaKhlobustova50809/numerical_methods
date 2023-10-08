# Метод исключения

A = [[2, 1, 4, 16], [3, 2, 1, 10], [1, 3, 3, 16]]
ans = []
a, b = len(A), len(A[0])

for i in range(a):
    d = A[i][i]
    for j in range(i, b):
        A[i][j] /= d
    for j in range(1, a):
        mn = A[(j+i) % 3][i]
        for k in range(i+1, b):
            A[(j+i) % 3][k] = A[(j+i) % 3][k] - mn*A[i][k]
        A[(j + i) % 3][i] = 0

for i in range(a):
    ans.append(A[i][b-1])
print(*ans)


