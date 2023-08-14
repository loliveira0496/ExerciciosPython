p = int(input("Quantas pessoas serao digitadas? "))

soma_a = 0
cont_i = 0
menores = []
for i in range(p):
    print(f"Dados da {i + 1}ª pessoa:")
    n = input("Nome: ")
    i = int(input("Idade: "))
    a = float(input("Altura: "))
    soma_a += a
    if i < 16:
        cont_i += 1
        menores.append(n)
media_a= soma_a / p
perc_i = (cont_i / p) * 100

print("")
print(f"Altura média: {media_a:.2f}")
print(f"Pessoas com menos de 16 anos: {perc_i:.1f}%")

for i in menores:
    print(i)