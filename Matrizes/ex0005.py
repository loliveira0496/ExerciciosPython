m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

matrizA = []
matrizB = []
matrizC = []

print("Digite os valores da matriz A: ")
for i in range(m):
    linha = []
    for j in range(n):
        e = int(input(f"Elemento{[i,j]}: "))
        linha.append(e)
    matrizA.append(linha)

print("Digite os valores da matriz B: ")
for i in range(m):
    linha = []
    for j in range(n):
        e = int(input(f"Elemento{[i,j]}: "))
        linha.append(e)
    matrizB.append(linha)

for i in range(m):
    linha = []
    for j in range(n):
      soma = matrizA[i][j] + matrizB[i][j]
      linha.append(soma)
    matrizC.append(linha)
print("MATRIZ SOMA:")
for i in matrizC:
    print("")
    for j in i:
      print(j, end=" ")

