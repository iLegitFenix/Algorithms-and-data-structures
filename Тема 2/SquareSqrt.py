def f(x):
    return x**2 + x**(1/2)

a = float(input())
exp = 1e-10
left = 0
right = a
for i in range(100):
    x = (left + right) / 2
    if abs(f(x) - a) > exp:
        if f(x) > a:
            right = x
        else:
            left = x
            
print(f'{x:.10f}')