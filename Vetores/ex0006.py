vetorA = []
vetorB = []
vetorC = []
q = int(input("Quantos valores vai ter cada vetor? "))

print("Digite os valores do vetor A: ")
for i in range(q):
    a = int(input())
    vetorA.append(a)

print("Digite os valores do vetor B: ")
for i in range(q):
    b = int(input())
    vetorB.append(b)

for i in range(q):
    soma = vetorA[i] + vetorB[i]
    vetorC.append(soma)

print("VETOR RESULTANTE: ")
for i in vetorC:
  print(i)