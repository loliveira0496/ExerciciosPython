n = int(input("Qual a ordem da matriz? "))

matriz = []
cont = 0
for i in range(n):
    linha = []
    for j in range(n):
      e = int(input(f"Elemento{[i,j]}: "))
      if e < 0:
         cont += 1
      linha.append(e)
    matriz.append(linha)

print("DIAGONAL PRINCIPAL")
for i in range(n):
   for j in range (n):
      if i == j:
         print(matriz[i][j], end=" ")
print("")
print(f"QUANTIDADE DE NEGATIVOS = {cont}")
