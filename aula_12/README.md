## OBJETIVOS
1. Receber a idade do aluno
2. Receber a nota da prova
3. Receber a frequência em %
4. Analise se a matricula pode ser aprovada
5. Exiba o resultado na tela

## REGRAS
A matricula será aprovada se:
# A idade >= 18 anos
# A nota >= 6
# A frequencia >= 75%

## REGRAS ESPECIAIS 
* Se a nota for >= 9 --> APROVADA AUTOMATICAMENTE
* Se a idade for <= 18 --> NEGADA AUTOMATICAMENTE

## LÓGICA ESPERADA
Se idade < 18
# negar matricula
Senao se nota >= 9
# aprovar automaticamente
Senao se idade >= 18 E nota >= 6  E frequencia >= 75
# aprovar matricula
Senao
# negar matricula