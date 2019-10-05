# -*- coding: utf-8 -*-

'''
    Class enum that represents a type of execution.
'''

from enum import Enum

class ExecutionType(Enum):
    MAIN = 1
    MAIN_WITHOUT_ARGS = 2
    RUN_ANALYSIS = 3