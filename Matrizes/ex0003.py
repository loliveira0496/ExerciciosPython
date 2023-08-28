m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

negativos = []
for i in range(m):
    lista = []
    for j in range(n):
        e = int(input(f"Elemento{[i,j]}: "))
        if e < 0:
            negativos.append(e)
print("VALORES NEGATIVOS: ")
for i in negativos:
    print(i)
