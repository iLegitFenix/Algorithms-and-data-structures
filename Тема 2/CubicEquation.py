def f(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d


a, b, c, d = map(int, input().split())
exp = 1e-15
left = -1e9
right = 1e9

for i in range(100):
    middle = (left + right) / 2
    if abs(f(a, b, c, d, middle)) > exp:
        if f(a, b, c, d, middle) * f(a, b, c, d, right) > 0:
            right = middle
        else:
            left = middle

print(f'{middle:.15f}')