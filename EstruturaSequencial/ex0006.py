n = input("Nome: ") 
vh = float(input("Valor por hora: "))
ht = float(input("Horas trabalhadas: ")) 
p = vh * ht
print(f"O pagamento para {n} deve ser {p:.2f}")
print("O pagamento para {} deve ser {:.2f}".format(n, p))
print("O pagamento para %s deve ser %.2f" % (n, p))
