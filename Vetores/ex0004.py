n = int(input("Quantos numeros voce vai digitar? "))
pares = []
cont = 0
for i in range(n):
    a = int(input("Digite um número: "))
    if a % 2 == 0:
        pares.append(a)
        cont += 1
print("")
print("NÚMEROS PARES: ")
for i in pares:
    print(i, end=" ")

print("")
print("")
print(f"QUANTIDADE DE PARES = {cont}")

