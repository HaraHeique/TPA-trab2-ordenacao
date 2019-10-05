# -*- coding: utf-8 -*-

import os, sys, handlerPerson, sortCollection as sort
from models.Person import Person
from models.ExecutionType import ExecutionType
from typing import List

def main():
    # Definição dos argumentos passados no CLI.
    args = handlerPerson.CLI_definition(sort.ALGORITHMS_SORTING_CHOICES)

    # Pega os nome do arquivo de entrada e saída. Caso estejam errados é lançado uma exceção
    input_filename: str = handlerPerson.check_filename(args.input)
    output_filename: str = handlerPerson.check_filename(args.output)

    # Extrai os objetos Person do arquivo.csv
    lst_person: List[Person] = handlerPerson.readCSV(input_filename)

    # Mensura o tempo de execução da CPU do processo de ordenação feita pelo algoritmo passado como argumento proveniente do CLI
    start_time: float = handlerPerson.get_cpu_time()
    sort.sort(lst_person, args.algorithm) if (args.algorithm != None) else sort.sort(lst_person)
    finish_time: float = handlerPerson.get_cpu_time()

    # Escreve o arquivo.csv de saída ordenado no mesmo modelo do arquivo.csv de entrada
    handlerPerson.writeCSV(lst_person, output_filename)

    # Reporta o tempo final de execução do processo de ordenação
    chosen_algorithm: str = args.algorithm if (args.algorithm != None) else 'quicksort'
    handlerPerson.report_time(chosen_algorithm, lst_person.__len__(), start_time, finish_time)

def main_without_args(lst_filenames: List[str]):
    for filename in lst_filenames:
        lstPerson: List[Person] = handlerPerson.readCSV(filename)
        sort.insertsort(lstPerson)
        handlerPerson.show_people(lstPerson)

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
    sys.tracebacklimit = 0
    choose_execution(ExecutionType.MAIN)
    