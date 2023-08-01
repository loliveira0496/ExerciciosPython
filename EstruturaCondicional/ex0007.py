print("Digite as tres distancias: ")
a = float(input())
b = float(input())
c = float(input())

maior = 0

if a > 0:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f"MAIOR DISTÂNCIA = {maior:.2f}")