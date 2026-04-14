# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

## Tipos de dados em python
1. string
2. number int
3. number float
4. boolean


## Operadores matemáticos - básicos
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão


## Operadores Lógicos
and -> e -> Se duas condições forem verdadeiras, o resultado é verdadeiro
ou -> or -> Se pelo menos uma condição for verdadeira, o resultado é verdadeiro
not -> Ele altera o valor booleano da condição


## Metódos em python
1. print() -> Exibe informções no terminal
2. input() -> Capturar uma informação no terminal


## Format em python


# Estrutura condicional
``if (se) ``-> Verifica se uma condição é true(verdadeira). Se for, ele executa o código
``elif (senão se) ``-> É usado para testar várias condições. Ele só executa se todas as condições anteriores forem falsas.
``else (senão)`` -> Executa o código se a condição if for false (falsa)


# Laços de Repetição
É o recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de Loop, Laços de repetição ou iteração.
`FOR` -> Utilizamos qundo sabemos quantas vees queremos repetir algo.
    Sintax Padrão:
`for variavel in range(inicio,fim):`
    comandos
[range()] -> Método que aceita gerações de números.
[início] -> É inclusivo. É o primeiro número a ser usado.
[fim] -> É exclusivo. O número utilizado é o anterior a esse.
    ## Escopo das Variáveis
Escopo Local -> A variável só é acessada dentro da estrutura que ela foi criada.
Escopo Global -> A variável pode ser acessada por todo mundo.


## Variações das variáveis
Variável em memória -> É declarada quando voce não pretende utilizar essa variável em outros cenários.
Variável contadora -> É utilizada para uma lógica onde a repetição irá ser alterada.

`WHILE` -> É utilizado quando não sabemos quantas vezes o programa vai repetir. Ele repete enquanto uma condição for verdadeira.
    Sintax:
`while condicao:`
    comandos


## Boas Práticas
1. Qualquer variável em Python utiliza o padrão de case snake_case ou recentemente o cammelCase.
2. Se você observar alguma estrutura tipo nome(), 90% de chance e ser uma função.
3. Python não tem constante, porém utilizamos o padrão case UPPERCASE, para simuLar que aquela variável não pode ser alterada.