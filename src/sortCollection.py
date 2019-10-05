# -*- coding: utf-8 -*-

'''
    A module responsible for sorting collections with many diferents types of algorithms.
'''

ALGORITHMS_SORTING_CHOICES: list = [
    "selectsort",
    "insertsort",
    "mergesort",
    "quicksort",
    "heapsort",
]

def sort(collection: list, algorithm_identifier: str = 'quicksort') -> None:
    '''
        Call a determined method by the algorithm identifier passed as argument 
        and sort the collection passed by reference.
    '''

    if algorithm_identifier == 'selectsort':
        selectsort(collection)
    elif algorithm_identifier == 'insertsort':
        insertsort(collection)
    elif algorithm_identifier == 'mergesort':
        raise NotImplementedError("Mergesort is not implemented yet. :(")
    elif algorithm_identifier == 'quicksort':
        raise NotImplementedError("Quicksort is not implemented yet. :/")
    elif algorithm_identifier == 'heapsort':
        raise NotImplementedError("Heapsort is not implemented yet. :(")
    elif algorithm_identifier == 'introsort':
        raise NotImplementedError("Introsort is not implemented yet. :/")
    elif algorithm_identifier == 'timsort':
        raise NotImplementedError("Timesort is not implemented yet. :(")
    elif algorithm_identifier == 'smoothsort':
        raise NotImplementedError("Smoothsort is not implemented yet. :/")
    elif algorithm_identifier == 'patiencesort':
        raise NotImplementedError("Patiencesort is not implemented yet. :(")
    else:
        raise NotImplementedError("Quicksort is not implemented yet. :/")

def selectsort(collection: list) -> None:
    '''O(n²) complexity sorting algorithm.'''

    collection_size: int = collection.__len__()

    for i in range(collection_size-1):
        indiceMenor = i
        k = i + 1

        while (k < collection_size):
            if (collection[k].compareTo(collection[indiceMenor])):
                indiceMenor = k
            k += 1
        
        if (indiceMenor != i):
            aux = collection[i]
            collection[i] = collection[indiceMenor]
            collection[indiceMenor] = aux

def insertsort(collection: list) -> None:
    '''O(n²) complexity sorting algorithm.'''

    collection_size: int = collection.__len__()

    for i in range(1, collection_size):
    	k: int = 0
    	while (collection[k].compareTo(collection[i]) and k < collection_size-1):
    		k += 1

    	if (collection[i].compareTo(collection[k])):
    		aux = collection[i]
    		del collection[i]
    		collection.insert(k, aux)


##################################### UNIT LIB TEST #####################################
def execute_test():
    pass

# Para testes unitários
if __name__ == '__main__':
    execute_test()