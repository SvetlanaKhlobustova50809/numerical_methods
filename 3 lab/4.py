# Метод простых итераций

A = [[2, 2, 10], [10, 1, 1], [2, 10, 1]]
B = [14, 12, 13]
a = len(A)

def maxind(arr):
    mm = arr[0]
    ind = 0
    for i in range(len(arr)-1):
        if mm < arr[i+1]:
            mm = arr[i+1]
            ind = i+1
    return ind

alf = [[0,0,0],[0,0,0],[0,0,0]]
bet = [0, 0, 0]

for i in range(a):
    t = maxind(A[i])
    for j in range(a):
        alf[t][j] = A[i][j]/A[i][t]*(-1)
        bet[t] = B[i]/A[i][t]
    alf[t][t] = 0

prov = []
for i in range(a):
    t = 0
    for j in range(a):
        t += alf[i][j]
    prov.append(abs(t))

if max(prov) < 1:

    x1 = bet.copy()
    x2 = []
    de = B.copy()
    for i in range(a):
        temp = 0
        for j in range(a):
            temp += x1[j]*alf[i][j]
        x2.append(temp+bet[i])
        de[i] = abs(x2[i] - x1[i])
    while max(de) >= 0.01:
        x1 = x2.copy()
        for i in range(a):
            temp = 0
            for j in range(a):
                temp += x1[j] * alf[i][j]
            x2[i] = round(temp + bet[i], 4)
            de[i] = abs(x2[i] - x1[i])

    print(*x2)
    for i in range(a):
        x2[i] = round(x2[i])
    print(*x2)
else:
    print(None)





