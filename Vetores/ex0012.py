q = int(input("Serao digitados dados de quantos produtos? "))
compra = []
venda = []
lucro = []
plucro = []

for i in range(q):
    print(f"Produto {i + 1}: ")
    n = input("Nome: ")
    pc = float(input("Preço de compra: "))
    compra.append(pc)
    pv = float(input("Preço de venda: "))
    venda.append(pv)
    l = pv - pc
    lucro.append(l)
    pl = ((pv - pc)/ pc) * 100
    plucro.append(pl)

contA = 0
contB = 0
contC = 0

for i in range (q):
    if plucro[i] < 10:
        contA += 1
    elif plucro[i] >= 10 and plucro[i] <= 20:
        contB += 1
    elif plucro[i] > 20:
        contC += 1

print(f"Lucro abaixo de 10%: {contA}")
print(f"Lucro entre 10 e 20%: {contB}")
print(f"Lucro acima de 20%: {contC}")
print(f"Valor total de compra: {sum(compra):.2f}")
print(f"Valor total de venda: {sum(venda):.2f}")
print(f"Lucro total: {sum(lucro):.2f}")


