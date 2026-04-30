p
while True:
    nome = input("\nDigite seu nome: \n")
    idade = int(input("\nDigite sua idade: \n"))
    convite = input("\nPossui convite? (sim/não)\n")

    print()
    print(f"Você se chama {nome}, possui {idade} anos e {convite} possui convite.")

    if idade < 16:
        print("Entrada Negada.")
    elif idade >= 16 and convite in ["sim", "Sim", "SIM", "s", "S"]: #a variável in aceita mais variações
        print("Entrada Permitida.")
    else:
        print("Entrada Negada.")

    sair = input("\nDigite SAIR para sair ou pressione Enter para continuar: ")
    if sair == "SAIR":
        break