n = int(input("Quantos numeros voce vai digitar? "))
soma = 0
contador = 0
valores = []
for i in range(n):
    numero = float(input("Digite um numero: " ))
    valores.append(numero)

print("")
print("VALORES = ", end="")
for i in valores:
    print(i, end="  ")
    soma += i
    contador += 1

print("")
print(f"SOMA = {soma:.2f}")
media = soma / contador
print(f"MÉDIA = {media:.2f}")