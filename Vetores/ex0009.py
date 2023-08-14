p = int(input("Quantas pessoas você vai digitar? "))

vetor_nome = []
vetor_idade = []
for i in range (p):
    print(f"Dados da {i + 1}a pessoa: ")
    nome = input("Nome: ")
    vetor_nome.append(nome)
    idade = int(input("Idade: "))
    vetor_idade.append(idade)

velho = 0
nome_velho = ""
for i in range(p):
    if vetor_idade[i] > velho:
       velho = vetor_idade[i]
       nome_velho = vetor_nome[i]

print(f"PESSOA MAIS VELHA: {nome_velho}")

