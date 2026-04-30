### Descrição do Desafio
Você deve criar um programa para uma escola que permita ao professor cadastrar vários alunos. O programa deverá solicitar o nome do aluno e 3 notas (de 0 a 10). Ao final, ele deve calcular a média de cada aluno, determinar sua situação ("Aprovado", "Recuperação" ou "Reprovado") e exibir um boletim completo para a turma.

### Requisitos Funcionais:
1. O programa deve primeiro perguntar quantos alunos serão cadastrados.🆗
2. Use um laço de repetição (`for` ou `while`) para solicitar os dados de cada aluno. 🆗
3. Para cada aluno, o programa deve pedir o **nome** e **três notas**. Armazene esses dados de forma organizada, utilizando uma lista principal para guardar os dados da turma. 🆗
4. Após coletar os dados de um aluno, calcule sua **média**. 🆗
5. Use uma estrutura condicional (`if`, `elif`, `else`) para determinar a **situação** do aluno com base nas seguintes regras:
    - **Aprovado:** Média >= 7.0
    - **Recuperação:** Média >= 5.0 e < 7.0
    - **Reprovado:** Média < 5.0 🆗
6. Ao final do cadastro de todos os alunos, o programa deve exibir um resumo da turma, mostrando o nome, as notas, a média e a situação de cada aluno.