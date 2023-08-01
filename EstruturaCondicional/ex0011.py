s = float(input("Digite o salario da pessoa: "))

if s > 0 and s <= 1000.00:
    ns =  s + (s * 0.20)
    a = s * 0.20
    p = int(0.20 * 100)
    print(f"Novo salário = {ns:.2f}")
    print(f"Aumento = {a:.2f}")
    print(f"Porcentagem = {p} %")

if s > 1000 and s <= 3000.00:
    ns =  s + (s * 0.15)
    a = s * 0.15
    p = int(0.15 * 100)
    print(f"Novo salário = {ns:.2f}")
    print(f"Aumento = {a:.2f}")
    print(f"Porcentagem = {p} %")

if s > 3000 and s <= 8000.00:
    ns =  s + (s * 0.10)
    a = s * 0.10
    p = int(0.10 * 100)
    print(f"Novo salário = {ns:.2f}")
    print(f"Aumento = {a:.2f}")
    print(f"Porcentagem = {p} %")

if s > 8000.00:
    ns =  s + (s * 0.05)
    a = s * 0.05
    p = int(0.05 * 100)
    print(f"Novo salário = {ns:.2f}")
    print(f"Aumento = {a:.2f}")
    print(f"Porcentagem = {p} %")

