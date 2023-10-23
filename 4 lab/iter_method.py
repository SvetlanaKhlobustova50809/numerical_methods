import numpy as np

def norm(arr):
    n = max(arr)
    for i in range(len(arr)):
        arr[i] /= n
    return arr

A = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]], dtype=np.float32)
ans = []
eps = 0.1
lenn = len(A)
X1 = np.array([], dtype=np.float32)

temp = []
for j in range(lenn):
    temp.append(1)
temp = np.array(temp)
X1 = np.append(X1, temp)
X2 = np.array(A.dot(X1), dtype=np.float32)
lam1 = X2[0]/X1[0]

X1 = np.copy(X2)
X2 = A.dot(X1)
lam2 = X2[0]/X1[0]

it = 1
while abs(lam1-lam2) > eps:
    lam1 = lam2.copy()
    X1 = np.copy(X2)
    X2 = A.dot(X1)
    lam2 = X2[0] / X1[0]
    it += 1
    if it % 3 == 0:
        X2 = norm(X2)
print(lam2)
print(X2)



