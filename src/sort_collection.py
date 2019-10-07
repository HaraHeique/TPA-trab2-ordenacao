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
        mergesort(collection)
    elif algorithm_identifier == 'quicksort':
        raise NotImplementedError("Quicksort is not implemented yet. :/")
    elif algorithm_identifier == 'heapsort':
        raise NotImplementedError("Heapsort is not implemented yet. :(")
    elif algorithm_identifier == 'introsort':
        raise NotImplementedError("Introsort is not implemented yet. :/")
    elif algorithm_identifier == 'timsort':
        raise NotImplementedError("Timsort is not implemented yet. :(")
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

def mergesort(collection: list) -> None:
    '''O(nlogn) complexity sorting algorithm.'''

    collection_size: int = collection.__len__()

    if (collection_size > 1):
        half: int = collection_size // 2
        
        lst_aux_left: list = collection[:half]
        lst_aux_right: list = collection[half:]

        mergesort(lst_aux_left)
        mergesort(lst_aux_right)
        __merge(collection, lst_aux_left,lst_aux_right)

        

def __merge(collection: list, lst_aux_left: list, lst_aux_right: list):
    i = j = k = 0

    while (i < lst_aux_left.__len__()) and (j < lst_aux_right.__len__()):
        if(lst_aux_left[i].compareTo(lst_aux_right[j])):
            collection[k] = lst_aux_left[i]
            i += 1
        else:
            collection[k] = lst_aux_right[j]
            j += 1
        k += 1

    for l in range(i, lst_aux_left.__len__()):
        collection[k] = lst_aux_left[l]
        k += 1

    for r in range(j, lst_aux_right.__len__()):
        collection[k] = lst_aux_right[r]
        k += 1


##################################### UNIT LIB TEST #####################################
def execute_test():
    pass

# Para testes unitários
if __name__ == '__main__':
    execute_test()