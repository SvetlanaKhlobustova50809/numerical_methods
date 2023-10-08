# Метод единичного деления

A = [[2, 1, 4, 16], [3, 2, 1, 10], [1, 3, 3, 16]]
ans = []
a, b = len(A), len(A[0])

for i in range(a):
    d = A[i][i]
    for j in range(i, b):
        A[i][j] /= d
    for j in range(i+1, a):
        mn = A[j][i]
        for k in range(i, b):
            A[j][k] -= A[i][k] * mn

for i in range(1, a+1):
    t = A[a - i][b-1]
    for j in range(1, i):
        t -= ans[j-1]*A[a-i][b-j-1]
    ans.append(t)

ans = list(reversed(ans))
print(*ans)

