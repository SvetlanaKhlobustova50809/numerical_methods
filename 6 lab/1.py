def divided_difference(f_values, x_values):
    n = len(f_values)
    F = [f_values.copy()]

    for k in range(1, n):
        F.append([(F[k - 1][i + 1] - F[k - 1][i]) / (x_values[i + k] - x_values[i]) for i in range(n - k)])

    return F

def newton_polynomial(x, x_values, F):
    n = len(x_values)
    result = F[0][0]

    for k in range(1, n):
        term = 1
        for i in range(k):
            term *= (x - x_values[i])
        result += F[k][0] * term

    return result

x_values = [0, 1, 2, 3]
f_values = [1, 2, 4, 1]
x_star = 1.5

F = divided_difference(f_values, x_values)
print(F)

result = newton_polynomial(x_star, x_values, F)

print(f"The value at x* = {x_star} is {result}")
