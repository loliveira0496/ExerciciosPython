c = int(input("Quantos casos de teste serao digitados? "))

coelhos = 0
ratos = 0
sapos = 0

for i in range(c):
    qc = int(input("Quantidade de cobaias: "))
    tc = input("Tipo de cobaia: ")

    if tc == 'c':
        coelhos += qc
    elif tc == 'r':
        ratos += qc
    elif tc == 's':
        sapos += qc

total = coelhos + ratos + sapos

pc = (coelhos / total) * 100 
pr = (ratos / total) * 100
ps = (sapos / total) * 100
print("")
print("RELATORIO FINAL: ")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {pc:.2f}")
print(f"Percentual de ratos: {pr:.2f}")
print(f"Percentual de sapos: {ps:.2f}")

