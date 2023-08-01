p = float(input("Preço unitário do produto:"))
q = int(input("Quantidade comprada: "))
d = float(input("Dinheiro recebido: "))

v = p * q

if v > d:
    troco = v - d
    print(f"DINHEIRO INSUFICIENTE. FALTAM {troco:.2f} REAIS")

else:
    troco = d - v
    print(f"TROCO = {troco:.2f} REAIS")

