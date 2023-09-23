import random

def f(x, ind):
    fun = 0
    for i in range(len(ind)): fun += ind[i]*x**i
    return fun

def Df(x, ind):
    fun = 0
    for i in range(1, len(ind)): fun += ind[i] * i * x ** (i-1)
    return fun

def newton_method(x0, ind):
    xn = x0
    while True:
        if Df(xn, ind) == 0:
            return None
        xn1 = xn - f(xn, ind) / Df(xn, ind)
        if abs(f(xn1, ind)) < 10 ** (-7):
            return xn1
        xn = xn1
    return None

ind = []
ind = list(map(float, input().split()))
print(newton_method(random.uniform(-1000, 1000), ind))
