xi = [3,4,5,6]
fi = [1,0,4,2]
x = 4.5

pr = 1
s = 0
di = 1
for i in range(4):
    pr *= x-xi[i]
    di = 1
    for j in range(4):
        if i == j:
            di *= x-xi[i]
        else:
            di *= xi[i] - xi[j]
    s += fi[i]/di

print(pr*s)
