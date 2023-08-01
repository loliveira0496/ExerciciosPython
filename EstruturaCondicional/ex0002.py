from math import sqrt, pow
a =float(input("Coeficiente a: " ))
b = float(input("Coeficiente b: " ))
c = float(input("Coeficiente c: " ))

d = pow(b, 2) - 4 * a * c

if d < 0:
    print("Esta equacao nao possui raizes reais ")

else:

    x1 = (-b + sqrt(d)) / 2 * a
    x2 = (-b - sqrt(d)) / 2 * a

    print(f"x1 = {x1:.3f}")
    print(f"x2 = {x2:.3f}")



