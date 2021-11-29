from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()

a, b, c = [int(input()) for _ in range(3)]
if a == 0:
    print(round(-c / b, 2))
else:
    d = b * b - 4 * a * c
    if d < 0:
        print('no roots')
    elif d == 0:
        print(round(-b / 2 / a, 2))
    else:
        print(round((-b - d ** 0.5) / 2 / a, 2))
        print(round((-b + d ** 0.5) / 2 / a, 2))