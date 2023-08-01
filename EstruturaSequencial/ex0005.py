from math import pow
r = float(input("Digite o valor do raio do circulo: "))
a = 3.14159 * pow(r, 2)

print(f"AREA = {a:.3f}")
print("AREA = {:.3f}".format(a))
print("AREA = %.3f" % a)
