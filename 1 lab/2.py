import random

def prit():
    b = []
    it = 0
    e = 10 ** (-7)
    b.append(random.uniform(0, 100))
    a = random.uniform(0, 100)
    b.append(0.5 * (a / b[it] + b[it]))
    it += 1

    while True:
        b.append(0.5 * (a / b[it] + b[it]))
        if abs((b[it+1] - b[it])/(1 - (b[it+1]-b[it])/(b[it]-b[it-1]))) < e:
            break
        it += 1

    return 0.5 * (a / b[it] + b[it])

print(prit())

