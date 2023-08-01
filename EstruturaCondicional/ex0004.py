m = float(input("Digite a quantidade de minutos: "))

if m > 100:
    v = (m - 100) * 2 + 50
    print(f"Valor a pagar: R$ {v:.2f}")
else:
    print("Valor a pagar: R$ 50.00")