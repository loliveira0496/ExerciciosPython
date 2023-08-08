v = int(input("Quantos numeros voce vai digitar? "))
count_dentro = 0
count_fora = 0
for i in range(v):
    n = int(input("Digite um número: "))
    if n >= 10 and n <= 20:
        count_dentro += 1
    else:
        count_fora += 1

print(f"{count_dentro} DENTRO")
print(f"{count_fora} FORA")