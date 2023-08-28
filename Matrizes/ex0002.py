m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))
somas = []
soma = 0
for i in range(m):
    print(f"Digite os elementos da {i + 1}ª linha: ")
    linha = []
    soma = 0
    for j in range(n):
      e = float(input())
      soma += e
    somas.append(soma)

print("VETOR GERADO: ")
for i in somas:
   print(i)  
