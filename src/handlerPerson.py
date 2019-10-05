# -*- coding: utf-8 -*-

'''
    Handles logic with Person model such as: data transformation, input CLI definitions,
    analysis logic and so on.
'''

import os, sys, csv, datetime, time
from models.Person import Person
from typing import List
from argparse import ArgumentParser

_INPUT_FILES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + "/files/input/"
_OUTPUT_FILES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + "/files/output/"

# Assim que o módulo é instanciado cria os diretórios de input e output de arquivos caso não existam
os.makedirs(_INPUT_FILES_PATH, exist_ok=True)
os.makedirs(_OUTPUT_FILES_PATH, exist_ok=True)

def CLI_definition(algorithm_choices: List[str]) -> object:
    '''
        Make the CLI definitions to start the application with correct 
        required and optional arguments.
    '''

    cli_parser: ArgumentParser = ArgumentParser()
    cli_parser.add_argument("input", type=str, help="Input: filename.csv")
    cli_parser.add_argument("output", type=str, help='Output: filename.csv')
    cli_parser.add_argument("-a", "--algorithm", type=str, 
                            choices=algorithm_choices, 
                            help="Choose the algorithm you would like to run. Default is quicksort")
    
    return cli_parser.parse_args()

def readCSV(input_filename: str) -> List[Person]:
    '''
        Read the content inside the filename passed as argument and transform 
        to the Person objects.
    '''

    try:
        lstPerson: List[Person] = []
        with open(_INPUT_FILES_PATH + input_filename, 'r') as csvfile:
            dataCSV = csv.reader(csvfile, delimiter=',')

            # Ignora a primeira linha do arquivo, pois é o header
            next(dataCSV)

            # Percorre pelas linhas instanciando o objeto da classe Person armazenando dentro da lista
            for dataRow in dataCSV: 
                lstPerson.append(Person(
                    dataRow[2], # id
                    dataRow[0], # email
                    dataRow[1], # gender
                    datetime.datetime.strptime(dataRow[3], "%Y-%m-%d"), # birthdate
                    int(dataRow[4]), # height
                    int(dataRow[5]), # weight
                ))
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)
    except IOError as err:
        print(err)
        sys.exit(1)
    except Exception as err:
        print(err)
        sys.exit(1)
    else:
        return lstPerson

def writeCSV(lst_person: List[Person], output_filename: str) -> None:
    '''Write the content in a CSV file for Person model.'''

    try:
        header: list = ["email", "gender", "uid", "birthdate", "height", "weight"]
        dataCSV: list = [header]
        for p in lst_person:
            dataCSV.append([
                p._email,
                p._gender,
                p._uid,
                p._birthdate.strftime("%Y-%m-%d"),
                p._height,
                p._weight
            ])
        with open(_OUTPUT_FILES_PATH + output_filename, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(dataCSV)
    except IOError as err:
        print(err)
        sys.exit(1)
    except Exception as err:
        print(err)
        sys.exit(1)

def check_filename(filename: str) -> str:
    '''Check if the filename is following the patterns and returns it if all is correct.'''

    file_array: List[str] = filename.split('.')
    if (file_array.__len__() != 2):
        raise Exception("Error: The filename has no extension or incorrect extension")

    if (file_array[1] != "csv"):
        raise Exception("Error: The filename extension must be .csv")

    return filename

def get_cpu_time() -> float:
    '''Returns the CPU time in milliseconds(ms) of the current process.'''

    return time.process_time() * 1000

def report_time(algorithm_identifier: str, total_records: int, start: float, finish: float) -> None:
    '''Reports whole CPU execution time.'''
    
    print("\nTime Execution Report:\n{0}\t{1} records\t{2}ms\n"
         .format(algorithm_identifier, total_records, finish-start))

def show_people(people: List[Person]):
    '''Print all people from the list.'''

    for p in people:
        print(p.toString())

##################################### UNIT LIB TEST #####################################
def execute_test():
    lstPerson: List[Person] = readCSV("data_10e0.csv")
    print(lstPerson.__len__())

def execute_test_writeCSV():
    import sortCollection
    lstPerson: list = readCSV("data_10e0.csv")
    sortCollection.insertsort(lstPerson)
    writeCSV(lstPerson, "data_10e0.csv")

# Para testes unitários
if __name__ == '__main__':
    pass
    #execute_test()
    #execute_test_writeCSV()