n = int(input("Quantos numeros voce vai digitar? "))

vetor = []
maior = 0
posicao = 0
for i in range(n):
    a = float(input("Digite um valor: "))
    vetor.append(i)
    if a > maior:
        maior = a
        posicao = vetor[i]

print(f"MAIOR VALOR = {maior}")
print(f"POSIÇÃO DO MAIOR VALOR = {posicao}")
    