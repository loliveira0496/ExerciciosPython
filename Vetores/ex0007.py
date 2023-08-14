q = int(input("Quantos elementos vai ter o vetor? "))
vetorA = []
soma = 0
for i in range(q):
    a = float(input("Digite um numero: "))
    vetorA.append(a)
    soma += a 

media = soma / q

print(f"MEDIA DO VETOR = {media:.3f}")
print("ELEMENTOS ABAIXO DA MÉDIA: ")
for i in vetorA:
    if i < media:
        print(i)
     