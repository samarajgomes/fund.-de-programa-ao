idade = int(input("Informe aqui sua idade: "))
nota = float(input("\nInforme aqui sua nota: \n"))
frequencia = float(input("\nInforme aqui sua frequencia (apenas números): \n"))

print()
print(f"Você tem {idade} anos, sua nota é {nota} e você obteve {frequencia}% de frequencia.")

if idade < 18:
    print("Infelizmente, sua matrícula não foi aprovada. É necessário ter mais de 18 anos.")
    print()
elif nota >= 9:
    print("Parabéns! Sua matrícula foi aprovada com sucesso.")
    print()
elif idade >= 18 and nota >= 6 and frequencia >= 75:
    print("Parabéns! Sua matrícula foi aprovada com sucesso.")
    print()
else:
    print("Infelizmente, sua matrícula não foi aprovada.")


