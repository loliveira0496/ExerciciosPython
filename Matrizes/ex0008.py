o = int(input("Qual a ordem da matriz? "))

matriz = []
soma = 0
diagonal = []
for i in range(o):
    linha = []
    for j in range(o):
      e = float(input(f"Elemento {[i,j]}: "))
      linha.append(e)
      if e > 0:
         soma += e
      if i == j:
         diagonal.append(e)
         
         
    matriz.append(linha)

print("")
print(f"SOMA DOS POSITIVOS: {soma}")
print("")
l = int(input("Escolha uma linha: "))
print(f"LINHA ESCOLHIDA: ", end=" ")
for i in range(o):
   for j in range(o):
      if i == l:
         print(matriz[i][j], end=" ")
print("")
print("")
c = int(input("Escolha uma linha: "))
print("COLUNA ESCOLHIDA: ", end=" ")
for i in range(o):
   for j in range(o):
      if j == c:
         print(matriz[i][j], end=" ")
print("")
print("")
print("DIAGONAL PRINCIPAL: ", end=" ")
for i in diagonal:
   print(i, end=" ")
print("")
print("")
print("MATRIZ ALTERADA: ")

      



