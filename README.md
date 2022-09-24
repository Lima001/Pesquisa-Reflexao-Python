# Pesquisa-Reflexao-Python
O presente repositório armazena os artefatos como suporte para a apresentação do trabalho **Uso de reflexão para verificação de tipos dinâmicos em objetos Python**, apresentado na Mostra de Ensino Pesquisa, Extensão e Cidadania 2022 (MEPEC 2022) do Instituto Federal Catarinense (IFC) Campus Blumenau.

## Trabalho apresentado

Em sequência apresenta-se o material que foi utilizado para apresentação da pesquisa. O conteúdo disposto na presente seção refere-se ao conteúdo que foi exibido em poster durante a MEPEC 2022. 

### Autores

- Gabriel Eduardo Lima
- [Hylson Vescovi Netto](https://github.com/hvescovi)

### Introdução

A pesquisa tem como objetivo discutir a possibilidade de usar recursos reflexivos na linguagem Python, visando realizar a checagem de tipos em objetos em uma linguagem de tipagem dinâmica. Como justificativa, a tipagem dinâmica é suscetível a erros de atribuição do tipo incorreto, e pode comprometer o sistema em tempo de execução. Reflexão computacional refere-se à capacidade de um sistema em conhecer a si próprio e o ambiente no qual está inserido, sendo capaz de manipulá-lo (MAES, 1987).

### Materiais e Métodos

O trabalho consistiu de uma pesquisa bibliográfica e de uma pesquisa exploratória, onde foi analisada a possibilidade de usar diferentes recursos do Python para construção de um mecanismo genérico e simples para realizar a checagem de tipos atribuídos aos objetos de uma classe. Por fim, decidiu-se aplicar o recurso de annotations por demonstrar ser útil no  contexto da pesquisa, uma vez que já é aplicado para especificar tipos de dados como forma de documentação.

### Resultados

Foi possível desenvolver um modelo reflexivo genérico. O mecanismo consiste em especificar os tipos dos parâmetros de um método X de uma classe A utilizando annotations, e invocar um outro método Y (genérico) de validação que recebe como parâmetros o método X que será analisado e os valores recebidos via parâmetros em X (Figura 1). A ideia fundamental consiste em acessar reflexivamente as metainformações annotations, verificando se os valores recebidos correspondem com o esperado. Caso não haja correspondência, o programador pode definir uma ação – como disparar um erro – que deve ser executada. Esse modelo pode ser aplicado, por exemplo, no construtor de uma classe para validar se os tipos dos dados usados para instanciar o objeto correspondem ao especificado pelo programador (Figura 2). Dessa forma, apenas objetos com tipos corretos são criados, caso contrário um erro descritivo é gerado, apontando a incoerência entre os tipos especificados e atribuídos (Figura 3).

[Figura 1](/imagens/img1.png)

[Figura 2](/imagens/img2.png)

[Figura 3](/imagens/img3.png)

### Conclusão

É possível utilizar reflexão para verificação de tipos em uma linguagem de tipagem dinâmica como Python. Além disso, destaca-se a possibilidade de criação de um modelo genérico de abstração para realizar essa funcionalidade. Por fim, como trabalhos futuros cita-se: Aprimoramento do modelo para tipos complexos – como listas; aplicação do mesmo conceito em
outras linguagens similares; implantação de um sistema real com o recurso em questão, analisando os impactos positivos e negativos do modelo.

### Referência
MAES P. Concepts and experiments in computational reflection. ACM SIGPLAN Notices, v. 22, n. 12, p. 147–155, 1987.