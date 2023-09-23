import random

def f(x, ind):
    fun = 0
    for i in range(len(ind)): fun += ind[i]*x**i
    return fun

def newton_method(x0, ind):
    xn = x0
    delta = 0.1
    Df = (f(x0, ind)-f(x0-delta, ind))/delta
    for i in range(10000000):
        xn1 = xn - f(xn, ind) / Df
        Df = (f(xn1, ind)-f(xn, ind))/(xn1-xn)
        if Df == 0:
            return None
        if abs(f(xn1, ind)) < 10 ** (-7):
            return xn1
        xn = xn1
    return None

ind = []
ind = list(map(float, input().split()))
print(newton_method(random.uniform(-1000, 1000), ind))
