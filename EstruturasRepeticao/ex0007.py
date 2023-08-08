contador = 0
soma = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n % 2 != 0:
        n += 1
    while contador <= 4:
        soma += n
        n += 2
        contador += 1
    break
print(f"SOMA = {soma}")