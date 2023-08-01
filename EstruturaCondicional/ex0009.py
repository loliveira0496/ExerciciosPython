c = int(input("Codigo do produto comprado: "))
q = int(input("Quantidade comprada: "))

if c == 1:
    resultado = 5.00 * q
    print(f"Valor a pagar: {resultado:.2f}")
elif c == 2:
    resultado = 3.50 * q
    print(f"Valor a pagar: {resultado:.2f}")
elif c == 3:
    resultado = 4.80 * q
    print(f"Valor a pagar: {resultado:.2f}")
elif c == 4:
    resultado = 8.90 * q
    print(f"Valor a pagar: {resultado:.2f}")
elif c == 2:
    resultado = 7.32 * q
    print(f"Valor a pagar: {resultado:.2f}")
else:
    print("Valor inválido!!!")
