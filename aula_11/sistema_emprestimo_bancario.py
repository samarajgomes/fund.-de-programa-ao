#Formando as variáveis cujo valores serão escritos na tela através do input
idade = int(input("\nInforme aqui sua idade: \n")) #É necessário converter os valores p/ número (int)
salario = int(input("\nInforme aqui seu salário: \n")) #/n quebra linha
tempo_trabalhado = int(input("\nInforme aqui seu tempo de trabalho (apenas numeros): \n"))

#P/ imprimir na tela c/ os valores
print()
print(f"Você possui {idade} anos, recebe {salario} reais e trabalha há {tempo_trabalhado} ano(s).")

#Calculando as condições: Idade >= 18 anos, Salário >= 2000, Tempo trabalhado >= 2 anos

if idade < 18:
    print("Infelizmente, no momento não foi possível aprovar seu empréstimo.")
    print()
elif salario >= 5000:
    print("Parabéns! Sua solicitação de empréstimo foi aprovado com sucesso.")
    print()
elif idade >= 18 and salario >= 2000 and tempo_trabalhado >= 2: #Em python, o operador lógico "and" é MINÚSCULO
    print("Parabéns! Sua solicitação de empréstimo foi aprovado com sucesso.")
    print()
else:
    print("Infelizmente, no momento não foi possível aprovar seu empréstimo.")


    ## EXTRA
# O int() só aceita números puros, sem texto.

#print() embaixo do print normal --> pula linha

#\n no começo e fimde dentro do parenteses do input quebra linha.
    

