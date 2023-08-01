p = float(input("Preço unitário do produto: "))
q = int(input("Quantidade comprada: "))

d = float(input("Dinheiro recebido: "))

t = d - (p * q)

print(f"TROCO = {t:.2f}")
print("TROCO = {:.2f}".format(t))
print("TROCO = %.2f" % t)
