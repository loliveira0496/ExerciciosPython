a = int(input("Quantas pessoas serao digitadas? "))

altura = []
genero = []
soma_alt_m = 0
cont_m = 0
cont_h = 0

for i in range(a):
  h = float(input(f"Altura da {i + 1}a pessoa: "))
  altura.append(h)
  g = input(f"Genero da {i + 1}a pessoa: ")
  genero.append(g)
  if g == 'F' or g == 'f':
    soma_alt_m += h
    cont_m += 1
  elif g == 'M' or g == 'm':
     cont_h += 1

media = soma_alt_m / cont_m
max_alt = max(altura)
min_alt = min(altura)

print(f"Menor altura = {min_alt}")
print(f"Maior altura = {max_alt}")
print(f"Media das alturas das mulheres = {media:.2f}")
print(f"Numero de homens = {cont_h}")


