n = int(input("Qual a ordem da matriz? "))
maior = []
for i in range(n):
    maior_linha = 0
    for j in range(n):
       e = int(input(f"Elemento{[i,j]}: "))
       if e > maior_linha:
           maior_linha = e
    maior.append(maior_linha)

print("MAIOR ELEMENTO DE CADA LINHA:")
for i in maior:
    print(i)
           