dp = float(input("Distancia percorrida: "))
cg = float(input("Combustível gasto: "))

cm = dp / cg

print(f"Consumo médio = {cm:.3f}")
print("Consumo médio = {:.3f}".format(cm))
print("Consumo médio = %.3f" % cm)

