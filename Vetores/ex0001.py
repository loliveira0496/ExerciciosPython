n = int(input("Quantos numeros voce vai digitar? "))

negativos = []

for i in range(n):
    numero = int(input("Digite um numero: " ))
    if numero < 0:
        negativos.append(numero)
print("NÚMEROS NEGATIVOS: ")
for i in negativos:
    print(i)

