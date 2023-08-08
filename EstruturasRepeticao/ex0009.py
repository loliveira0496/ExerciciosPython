print("Digite dois numeros: ")
n1 = int(input()) 
n2 = int(input())
soma_impar = 0
aux = 0
if n1 > n2:
    aux = n2
    n2 = n1
    n1 = aux
for i in range(n1+1,n2):
    if i % 2 != 0:
        soma_impar += i
print(f"SOMA DOS IMPARES = {soma_impar}")


