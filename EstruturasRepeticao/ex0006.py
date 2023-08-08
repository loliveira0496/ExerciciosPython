a = 0
g = 0
d = 0
while True:
    c = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))
    if c == 4:
        break
    elif c == 1:
        a += 1
    elif c == 2:
        g += 1
    elif c == 3:
        d += 1

print(f"Álcool: {a}")     
print(f"Gasolina: {g}") 
print(f"Diesel: {d}")         