import random

def f(x, ind):
    fun = 0
    for i in range(len(ind)): fun += ind[i]*x**i
    return fun

def Df(x, ind):
    fun = 0
    for i in range(1, len(ind)): fun += ind[i] * i * x ** (i-1)
    return fun

def newton_method(x0, ind, con):
    xn = x0
    for i in range(10000000):
        if Df(xn, ind) == 0:
            return None
        xn1 = xn - con * f(xn, ind) / Df(xn, ind)
        if abs(f(xn1, ind)) < 10 ** (-7):
            return xn1
        xn = xn1
    return None

ind = []
ind = list(map(float, input().split()))
con = float(input())
print(newton_method(random.uniform(-1000, 1000), ind, con))
