n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

nf = n1 + n2

print(f"NOTA FINAL = {nf:.1f}")
print("NOTA FINAL = {:.1f}".format(nf))
print("NOTA FINAL = %.1f" % nf)

if nf < 60.0:
    print("REPROVADO")
else:
    print("APROVADO")

