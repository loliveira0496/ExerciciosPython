t = input("Voce vai digitar a temperatura em qual escala (C/F)?")
if t == 'c' or t == 'C':
    c = float(input("Digite a temperatura em Celsius:" ))
    f = (9 * c + 160) / 5
    print(f"Temperatura equivalente em Fahrenheit: {f:.2f}")
elif t == 'f' or t == 'F':
    f = float(input("Digite a temperatura em Fareheint: "))
    c = 5 / 9 *(f-32)
    print(f"Temperatura equivalente em Celsius: {c:.2f}")