xi = [3,4,5,6]
fi = [1,0,4,2]
x = 4.5

k1 = -1
for i in range(len(xi)-1):
    if xi[i] < x and xi[i+1] > x:
        k1 = i-1

l12 = 0
l22 = 0
if k1 != -1:
    k2 = k1 + 1
    for i in range(3):
        l12 += ((x - xi[k1 + (1 + i) % 3]) * (x - xi[k1 + (2 + i) % 3])) / (
                    (xi[k1 + i] - xi[k1 + (1 + i) % 3]) * (xi[k1 + i] - xi[k1 + (2 + i) % 3])) * fi[k1 + i]
        l22 += ((x - xi[k2 + (1 + i) % 3]) * (x - xi[k2 + (2 + i) % 3])) / (
                    (xi[k2 + i] - xi[k2 + (1 + i) % 3]) * (xi[k2 + i] - xi[k2 + (2 + i) % 3])) * fi[k2 + i]
    print((l12+l22)/2)
else:
    print(None)
