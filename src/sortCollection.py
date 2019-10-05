# -*- coding: utf-8 -*-

'''
    A module responsible for sorting collections with many diferents types of algorithms.
'''

def sort(collection: list, algorithmId: str = 'quicksort') -> None:
    '''Call a determined method by the algorithm identifier passed as argument.'''

    if algorithmId == 'selectsort':
        selectsort(collection)
    elif algorithmId == 'insertsort':
        insertsort(collection)
    elif algorithmId == 'mergesort':
        raise NotImplementedError()
    elif algorithmId == 'quicksort':
        raise NotImplementedError()
    elif algorithmId == 'heapsort':
        raise NotImplementedError()
    elif algorithmId == 'introsort':
        raise NotImplementedError()
    elif algorithmId == 'timsort':
        raise NotImplementedError()
    elif algorithmId == 'smoothsort':
        raise NotImplementedError()
    elif algorithmId == 'patiencesort':
        raise NotImplementedError()
    else:
        raise NotImplementedError()

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