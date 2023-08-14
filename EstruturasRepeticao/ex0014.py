casos = int(input("Quantos casos você vai digitar? "))

for i in range(casos):
    print("Entre com o numerador:")
    a = float(input())
    print("Entre com o denominador:")
    b = float(input())
    
    if b == 0:
        print("DIVISÃO IMPOSSÍVEL")
    else:
        div = a / b
        print(f"DIVISÃO = {div:.2f}")
