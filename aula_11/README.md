## OBJETIVO
Criar um programa para analisar se um cliente pode receber um empréstimo

## INFORMAÇÕES
Idade do Cliente
Salário do Cliente
Tempo trabalhado

# Idade >= 18 anos
# Salário >= 2000
# Tempo trabalhado >= 2 anos

## REGRAS ESPECIAIS
Sálario >= 5000 -> Aprovação Automática
Idade < 18 -> Empréstimo Negado

# DICA DE LÓGICA -- SEGUIR ESSA SEQUÊNCIA
Idade < 18? -- Negar
Salário >= 5000? -- Aprovar
Idade >= 18 E Sálario >= 2000 E Tempo >= 2 -- Aprovar SENAO -- Negar