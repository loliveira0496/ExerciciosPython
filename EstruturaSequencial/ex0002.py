from math import sqrt, pow
b = float(input("Base do retangulo: "))
h = float(input("Altura do retangulo:"))

a = b * h
p = (2 * b) + (2 * h)
d = sqrt(pow(b, 2) + pow(h, 2))

print(f"AREA = {a:.4f}")
print(f"PERIMETRO = {p:.4f}")
print(f"DIAGONAL = {d:.4f}")

print("AREA = {}".format(a))
print("PERIMETRO = {}".format(p))
print("DIAGONAL = {}".format(d))

print("AREA = %.4f" % a)
print("PERIMETRO = %.4f" % p)
print("DIAGONAL = %.4f" % d)
