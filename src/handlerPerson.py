# -*- coding: utf-8 -*-

'''
    Handles logic with Person class data transformation
'''

import os, sys, csv, datetime
from models.Person import Person

_INPUT_FILES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + "/files/input/"
_OUTPUT_FILES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + "/files/output/"

def readCSV(inputFileName: str) -> list:
    '''Read the content inside the filename passed as argument and transform to the Person objects.'''

    try:
        lstPerson: list = []
        with open(_INPUT_FILES_PATH + inputFileName, 'r') as csvfile:
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

def writeCSV(lstPerson: list, outputFileName: str) -> None:
    '''Write the content in a CSV file for Person model.'''

    try:
        header: list = ["email", "gender", "uid", "birthdate", "height", "weight"]
        dataCSV: list = [header]
        for p in lstPerson:
            dataCSV.append([
                p._email,
                p._gender,
                p._uid,
                p._birthdate.strftime("%Y-%m-%d"),
                p._height,
                p._weight
            ])
        with open(_OUTPUT_FILES_PATH + outputFileName, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(dataCSV)
    except IOError as err:
        print(err)
        sys.exit(1)
    except Exception as err:
        print(err)
        sys.exit(1)

def show_people(people: list):
    for p in people:
        print(p.toString())

##################################### UNIT LIB TEST #####################################
def execute_test():
    lstPerson: list = readCSV("data_10e0.csv")
    print(lstPerson.__len__)

def execute_test_writeCSV():
    import sortCollection
    lstPerson: list = readCSV("data_10e0.csv")
    sortCollection.insertsort(lstPerson)
    writeCSV(lstPerson, "data_10e0.csv")

# Para testes unitários
if __name__ == '__main__':
    execute_test()
    execute_test_writeCSV()