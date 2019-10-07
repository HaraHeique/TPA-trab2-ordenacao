# -*- coding: utf-8 -*-

import os, sys, handler_person, sort_collection as sort
from models.Person import Person
from models.ExecutionType import ExecutionType
from typing import List

def main():
    # Definição dos argumentos passados no CLI.
    args = handler_person.CLI_definition(list(sort.ALGORITHMS_SORTING_CHOICES.keys()))

    # Pega os nome do arquivo de entrada e saída. Caso estejam errados é lançado uma exceção
    input_filename: str = handler_person.check_filename(args.input)
    output_filename: str = handler_person.check_filename(args.output)

    # Extrai os objetos Person do arquivo.csv
    lst_person: List[Person] = handler_person.readCSV(input_filename)

    # Mensura o tempo de execução da CPU do processo de ordenação feita pelo algoritmo passado como argumento proveniente do CLI
    start_time: float = handler_person.get_cpu_time()
    sort.sort(lst_person, args.algorithm) if (args.algorithm != None) else sort.sort(lst_person)
    finish_time: float = handler_person.get_cpu_time()

    # Escreve o arquivo.csv de saída ordenado no mesmo modelo do arquivo.csv de entrada
    handler_person.writeCSV(lst_person, output_filename)

    # Reporta o tempo final de execução do processo de ordenação
    chosen_algorithm: str = args.algorithm if (args.algorithm != None) else 'quicksort'
    handler_person.report_time(chosen_algorithm, lst_person.__len__(), start_time, finish_time)

def main_without_args(lst_filenames: List[str]):
    for filename in lst_filenames:
        lstPerson: List[Person] = handler_person.readCSV(filename)
        sort.mergesort(lstPerson)
        handler_person.show_people(lstPerson)

# TODO Script de execução automática dos testes de análise
def run_analysis():
    pass

def choose_execution(execution_type: ExecutionType):
    if (execution_type == ExecutionType.MAIN):
        main()
    elif (execution_type == ExecutionType.MAIN_WITHOUT_ARGS):
        lstFileNames: list = [
            "data_10e0.csv"
        ]
        main_without_args(lstFileNames)
    elif (execution_type == ExecutionType.RUN_ANALYSIS):
        pass
    else:
        raise Exception("Invalid execution type.")

if __name__ == '__main__':
    sys.tracebacklimit = 1
    choose_execution(ExecutionType.MAIN)
    