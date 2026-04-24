
## 1. Inicie o programa com uma variável saldo com um valor inicial (ex: 1000.00) e uma lista vazia chamada historico para registrar as transações.
saldo = 1000.00  # Váriavel number tpo float
historico = [] # Lista vazia

print(f'🏧 --- Bem-vindo ao Caixa Eletrônico ---')

## 2. Crie um laço de repetição while que mantenha o programa ativo e exiba o seguinte menu de opções:
while True: # Imprime pelo menos o while uma vez
    print(f''' --- Menu Principal ---
          [1] - Depositar
          [2] - Sacar
          [3] - Ver Saldo
          [4] Ver Histórico
          [5] - Sair
        ''')
    opcao = input(' ➡️ Escolha uma opção: ') # Escopo global: só existe dentro do while

## 3. Depositar: Se o usuário escolher [1], o programa deve pedir o valor a ser depositado, atualizar o saldo e adicionar uma entrada ao historico (ex: "Depósito: +R$ 50.00").
    # Lógica para a opção de Depósito
    if opcao == '1':
        valor_deposito = float(input(' ➡️ Digite o valor para Depósito: R$'))

        # Verificar o valor do depósito para ver se é maior 0 ou não:
        if valor_deposito > 0:
            saldo = saldo + valor_deposito # Ou usa +=
            registro = f'Depósito: +R$ {valor_deposito:.2f}' #2f: Quer que tenha 2 casas decimais
            #Incluir no historico
            historico.append(registro) # append() adicionar algo na lista
            print('🆗 Depósito realizado com sucesso!')

        # Qualquer coisa que ele digite que não seja maior que 0:
        else:
            print('❌ Valor inválido! O Depósito deve ser um número positivo.')

## 4. Sacar: Se o usuário escolher [2], o programa deve pedir o valor do saque. **Utilize uma estrutura condicional** para verificar se o `saldo` é suficiente.
    #- Se for suficiente, atualize o `saldo`, registre no `historico` (ex: "Saque: -R$ 100.00") e informe que o saque foi bem-sucedido.
    #- Se não for suficiente, não altere o saldo e exiba uma mensagem de "Saldo insuficiente".
    elif opcao == '2':
        valor_saque = float(input(' ➡️ Digite o valor para Saque: R$'))

        # Estrutura condicional para verificar se o saldo é suficiente
        if valor_saque <= 0:
            print('❌ Valor inválido! O Depósito deve ser um número positivo.')

        # Se o saque for maior que o saldo, não é possivel fazer o saque
        elif valor_saque > saldo:
            print('❌ Valor inválido! O Depósito deve ser um número positivo.')
        else:
            saldo -= valor_saque
            registro = f'Saque: -R$ {valor_saque:.2f}'
            historico.append(registro)
            print('🆗 Saque realizado com sucesso! Retire o seu dinheiro.')

## Ver Saldo: Se o usuário escolher [3], apenas exiba o valor atual do saldo.
    elif opcao =='3':
        # Passar o valor do saldo atual:
        print(f'💰 Seu saldo atual é: {saldo:.2f}')

## Ver Histórico: Se o usuário escolher [4], exiba todas as transações registradas na lista historico.
    elif opcao =='4':
        print('📃 --- Histórico de Transações ---')
        if not historico: # Verifica se histórico está vazio, pois toda variável/estrutura vazia é True por padrão
            print('❌ Nenhuma transação foi realizada ainda.')
        else:
            for transacao in historico: # O 'transacao' poderia ter qualquer nome. Variável coringa que chama cada informação que está dentro da variavel por vez
                print(transacao)

## Sair: Se o usuário escolher [5], o laço while deve ser interrompido e o programa encerrado com uma mensagem de despedida.
    elif opcao == '5':
        print('😊 Obrigado por utilizar nosso Caixa Eletrônico. Finalizando ...')
        break # Encerra o laço while
    # Caso o usuario nao digite nenhum dos numeros indicados
    else:
        print('❌ Opção Inválida. por favor, escolha uma das opções do menu.')
