e = int(input("Quantos elementos vai ter o vetor? "))
soma = 0
cont_par = 0
cont_impar = 0
media_pares = 0
for i in range(e):
    n = float(input("Digite um número: "))
    if n % 2 == 0:
        soma += n
        cont_par += 1
        media_pares = soma / cont_par
        print(f"MÉDIA DOS PARES = {media_pares:.1f}")
    else:
        cont_impar += 1
    
if cont_impar == e:
    print("NENHUM NÚMERO PAR")