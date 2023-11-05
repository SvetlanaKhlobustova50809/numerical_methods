xi = [3,4,5,6]
fi = [1,0,4,2]
x = 4.5

k1 = -1
for i in range(len(xi)-1):
    if xi[i] < x and xi[i+1] > x:
        k1 = i

if k1 != -1:
    p1i = (x-xi[k1+1])/(xi[k1]-xi[k1+1])
    p1i1 = (x-xi[k1])/(xi[k1+1]-xi[k1])
    if p1i+p1i1 == 1:
        f = p1i*fi[k1]+p1i1*fi[k1+1]
        print(f)
    else:
        print(None)
else:
    print(None)

