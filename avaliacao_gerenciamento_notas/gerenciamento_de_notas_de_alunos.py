## perguntando quantos alunos serão cadastrados
alunos_cadastrados = int(input("Quantos alunos deseja cadastrar? "))
turma = [] # lista vazia

print("\n--- Dados dos Alunos ---")

contador = 0 # variável que conta quantas vezes o loop já aconteceu.

## usando laço de repetição para cadastrar cada aluno
while True:

    nome = input("\nInsira o nome do aluno: \n")
    nota1 = float(input("Insira a primeira nota do aluno: "))
    nota2 = float(input("Insira a segunda nota do aluno: "))
    nota3 = float(input("Insira a terceira nota do aluno: "))

    # calculando a média das notas
    media = (nota1 + nota2 + nota3) / 3

    # definindo situação
    if media >= 7.0:
        situacao = "aprovado(a)" 
    elif media >= 5.0 and media < 7.0:
        situacao = "de recuperação"
    else:
        situacao = "reprovado(a)"
    
    # incluindo dados na lista principal
    turma.append([nome, nota1, nota2, nota3, media, situacao])

    print(f"{nome} está {situacao} com média {media:.2f}.")
    
    contador += 1 # 1 soma 1 a cada aluno para controlar quando parar o programa

    # condição p parar o programa quando cadastrar todos os alunos que o usuário pediu
    if contador == alunos_cadastrados: 
        break

# resumo da turma
print("\n--- Resumo da Turma ---\n")

for aluno in turma: #mostrar todos os alunos da lista, um por um (percorrer a lista)
    print(f"Nome: {aluno[0]}") # os numeros se referem a: nome, nota1, nota2, nota3, media e situacao, respectivamente
    print(f"Notas: {aluno[1]}, {aluno[2]}, {aluno[3]}") 
    print(f"Média: {aluno[4]:.2f}")
    print(f"Situação: {aluno[5]}")