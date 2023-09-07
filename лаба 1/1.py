import random

def func(x):
    return (x-2)*((x-3)*(x-3))*(x-7)

def poldel():
    e = 0.01
    a = random.uniform(2, 7)
    b = random.uniform(-100, 0)
    if func(a)*func(b) >= 0:
        return None
    while abs(a-b) >= e:
        c = (a+b)/2
        if func(a)*func(c) < 0:
            b = c
        if func(b)*func(c) < 0:
            a = c
    return (a+b)/2

print(poldel())

