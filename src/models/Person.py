# -*- coding: utf-8 -*-

'''
    Class representing a Person
'''

from datetime import date, datetime

class Person:
    def __init__(self, id: str, email: str, gender: str, birthdate: date, height: int, weight: int):
        self._email: str = email
        self._gender: str = gender
        self._uid: str = id
        self._birthdate: date = birthdate
        self._height: int = height
        self._weight: int = weight

    @property
    def id(self) -> str:
        return self._uid

    @property
    def email(self) -> str:
        return self._email

    def compareTo(self, person) -> bool:
        '''
            Returns True if the self object(the caller) is less than the Person object passed as argument.
            Otherwise returns False
        '''
        if (self._uid < person._uid):
            return True
        return False

    def toString(self) -> str:
        '''A string representation to Person model'''
        return "UID: {0}\t Email: {1}\t Gender: {2}".format(self._uid, self._email, self._gender)

##################################### UNIT CLASS TEST #####################################
def execute_test():
    person: Person = Person(
        "7561ED8641FBFDEB",
        "teste123@gmail.com",
        'M',
        datetime.strptime("1998-02-07", "%Y-%m-%d"),
        182,
        89
    )
    print(person._birthdate)

# Para testes unitários
if __name__ == '__main__':
    execute_test()