a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: ")) 
c = int(input("Terceiro valor: ")) 

menor = 0
# maior = 0

if a > menor or a < 0:
    menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

print(f"MENOR = {menor}")