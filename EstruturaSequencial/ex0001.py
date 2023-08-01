h = float(input("Digite a largura do terreno: ")) 
w = float(input("Digite o comprimento do terreno:")) 
sm = float(input("Digite o valor do metro quadrado:")) 

a = h * w
p = sm * a

print(f"Área do terreno = {a:.2f}")
print(f"Preco do terreno = {p:.2f}")

print("Área do terreno = {:.2f}".format(a))
print("Preco do terreno = {:.2f}".format(p))

print("Área do terreno = %.2f" % a)
print("Preco do terreno = %.2f" % p)

