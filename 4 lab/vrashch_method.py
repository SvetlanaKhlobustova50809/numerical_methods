import numpy as np
import math

def maxx(A):
    a = A[0][1]
    ki = 0
    kj = 1
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if max(a, A[i][j]) != a:
                kj = j
                ki = i
            a = max(a, A[i][j])
    return a, ki, kj

def fillH(lenn,ki,kj,sinalf,cosalf):
    H = []
    for i in range(lenn):
        t = []
        for j in range(lenn):
            if i == j and (i == ki or i == kj):
                t.append(cosalf)
            elif i == ki and j == kj:
                t.append(-sinalf)
            elif i == kj and j == ki:
                t.append(sinalf)
            elif i == j:
                t.append(1)
            else:
                t.append(0)
        H.append(t)
    return H

A = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]], dtype=np.float32)
eps = 0.001
lenn = len(A)

a = A[0][1]
ansmat = np.array([], dtype=np.float32)

flag = True
while abs(a) > eps:
    a, ki, kj = maxx(A)
    if A[ki][ki] == A[kj][kj]:
        alf = math.pi/4
    else:
        alf = 1/2*math.atan(2*A[ki][kj]/(A[ki][ki]-A[kj][kj]))
    sinalf = math.sin(alf)
    cosalf = math.cos(alf)
    H = fillH(lenn, ki, kj, sinalf, cosalf)
    H = np.array(H, dtype=np.float32)
    if flag:
        H1 = np.copy(H)
    else:
        H1 = np.dot(H1, H)
    Htran = np.transpose(H)
    A = np.dot(Htran, A)
    A = np.dot(A, H)
    flag = False

sobsznach = []
vec = []
for i in range(lenn):
    sobsznach.append(A[i][i])
print("Собственные значения:", *sobsznach)
print("Собсвенные вектора:")
for i in range(lenn):
    vec = []
    for j in range(lenn):
        vec.append(H1[j][i])
    print(vec)





