# -*- coding: utf-8 -*-

import argparse, os, sys, enum, handlerPerson, sortCollection as sort
from models.Person import Person
from models.ExecutionType import ExecutionType

# OBS.: Pegando os argumentos do terminal sem o argparse
def main(args: list):
    inputFileName: str = args[1]
    lstPerson: list = handlerPerson.readCSV(inputFileName)

def main_without_args(lstFileNames: list):
    for fileName in lstFileNames:
        inputFileName: str = fileName
        lstPerson: list = handlerPerson.readCSV(inputFileName)
        sort.insertsort(lstPerson)
        handlerPerson.show_people(lstPerson)

def run_analysis():
    pass

def choose_execution(execution_type: ExecutionType):
    if (execution_type == ExecutionType.MAIN):
        main(sys.argv)
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
    choose_execution(ExecutionType.MAIN_WITHOUT_ARGS)
    