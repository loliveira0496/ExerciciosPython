a = int(input("Quantos alunos serao digitados? "))
nome = []
nota1 = []
nota2 = []
medias = []
for i in range(a):
    print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
    n = input()
    nome.append(n)
    n1 = float(input())
    nota1.append(n1)
    n2 = float(input())
    nota2.append(n2)
    media = (nota1[i] + nota2[i]) / 2
    medias.append(media)
print("Alunos aprovados: ")

for i in range(a):
    if medias[i] >= 6.0:
        print(nome[i])
