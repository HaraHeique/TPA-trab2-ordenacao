# Trabalho 2 de TPA 2019/2 - Algoritmos de Ordenação

O trabalho em questão é da disciplina de *TPA (Técnicas de Programação Avançada)*, do curso de graduação de Bacharelado de Sistema de Informação do IFES - Serra, pelo docente Dr. Jefferson Oliveira Andrade.

### Informações gerais
- **Autores**: David Vilaça, Harã Heique e Larissa Motta
- **Linguagem de programação**: Python (versão 3.6.8+)
- **Ferramentas de suporte**: Nenhuma (por enquanto)
- **Ambiente de desenvolvimento**: Visual Studio Code (versão 1.35.1+)

A ordenação é um dos problemas algorı́tmicos mais fundamentais da ciência da computação. Já foi afirmado que até 25% de todos os ciclos de CPU são usados para ordenação, o que fornece um grande incentivo para estudos adicionais e otimização sobre
ordenação. Dado isso o trabalho consiste na implementação de algoritmos de ordenação, assim como análises de suas perfomances.

No escopo do trabalho é necessário implementar sete dos nove algoritmos de ordenação propostos, os quais escolhidos estão em negrito abaixo:
- **Insertion sort**
- **Selection sort**
- **Merge Sort**
- **Quicksort**
- **Heapsort**
- **Introsort**
- **Timsort**
- Smoothsort
- Patience sorting

### Descrição geral
A estrutura da aplicação está definida da seguinte maneira:

```
TPA-trab2-ordenacao
|_ README.md
|_ relatório.pdf
|_ codes-references.txt
|_ src
    |_ analisys_person.py
    |_ build.py
    |_ handler_person.py
    |_ sort_collection.py
    |_ files
        |_ input
            |_ *arquivos entrada*.csv
        |_ output
            |_ *arquivos saída*.csv
        |_ analyze
            |_ *arquivos saída dos testes da análise*.csv
    |_ models
        |_ ExecutionType.py
        |_ Person.py
```

### Como executar?
Para buildar/executar o app no ambiente Linux, onde a linguagem Python geralmente já vem instalado nativamente, basta abrir o CLI(Command Line Interface) no diretório __/src__ e digitar o seguinte comando:

    $ python3 build.py --input arquivo_entrada.csv --output arquivo_saida.csv --algorithm identificador_algoritmo
    Ou
    $ python3 build.py --input arquivo_entrada.csv --output arquivo_saida.csv -a identificador_algoritmo
    Ou
    $ python3 build.py --input arquivo_entrada.csv --output arquivo_saida.csv

Note que o nome dos arquivos tanto de entrada, precedidos de *--input*, quanto de saída, precedidos de *--output*, são **obrigatórios**. Caso não sejam passados será lançada uma exceção explicando formas de ser executada de maneira correta. Também há a possibilidade de utilização do comando abaixo que também fornecerá informações para o correto comando de execução do app.

    $ python3 build.py --help
    Ou
    $ python3 build.py -h

Já o identificador do algoritmo é um argumento **opcional** precedido de *-a*, quando abreviado, ou *--algorithm*, sem abreviação. Logo quando este parâmetro não é fornecido o **algoritmo de ordenação default é o Quicksort**. Quanto aos identificadores de algoritmo (*identificador_algoritmo*) podem ser utilizados os seguintes:

<div align="center">
  
Algoritmo|Identificador
---|---
**Selection sort**|selectsort
**Insert sort**|insertsort
**Merge Sort**|mergesort
**Quicksort**|quicksort
**Heapsort**|heapsort
**Introsort**|introsort
**Timsort**|timsort

</div>


### Informações adicionais
Todo o código fonte está hospedado no [GitHub](https://github.com/HaraHeique/TPA-trab2-ordenacao).
