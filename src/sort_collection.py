# -*- coding: utf-8 -*-
import math

'''
    A module responsible for sorting collections with many diferents types of algorithms.
'''

ALGORITHMS_SORTING_CHOICES: dict = {
    "selectsort": "Selection Sort",
    "insertsort": "Insertion Sort",
    "mergesort": "Merge Sort",
    "quicksort": "Quicksort",
    "heapsort": "Heapsort",
    "introsort": "Introsort",
    # "timsort": "Timsort",
}


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
        quicksort(collection)
    elif algorithm_identifier == 'heapsort':
        heapsort(collection)
    elif algorithm_identifier == 'introsort':
        introsort(collection)
    elif algorithm_identifier == 'timsort':
        raise NotImplementedError("Timsort is not implemented yet. :(")
    elif algorithm_identifier == 'smoothsort':
        raise NotImplementedError("Smoothsort is not implemented yet. :/")
    elif algorithm_identifier == 'patiencesort':
        raise NotImplementedError("Patiencesort is not implemented yet. :(")
    else:
        quicksort(collection)


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
        k: int = i-1
        aux: object = collection[i]

        while (k >= 0 and aux.compareTo(collection[k])):
            collection[k+1] = collection[k]
            k -= 1

        if (k+1 != i):
            collection[k+1] = aux


def mergesort(collection: list) -> None:
    '''O(nlogn) complexity sorting algorithm.'''

    collection_size: int = collection.__len__()

    if (collection_size > 1):
        half: int = collection_size // 2

        lst_aux_left: list = collection[:half]
        lst_aux_right: list = collection[half:]

        mergesort(lst_aux_left)
        mergesort(lst_aux_right)
        __merge(collection, lst_aux_left, lst_aux_right)


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


def quicksort(collection: list) -> None:
    __quicksort(collection, 0, len(collection) - 1)


def __quicksort(collection: list, left: int, right: int) -> None:
    if (left < right):
        partitionI: int = __partition(collection, left, right)
        __quicksort(collection, left, partitionI - 1)
        __quicksort(collection, partitionI + 1, right)

# elements swap by indexes


def __swap(collection: list, i: int, j: int) -> None:
    collection[i], collection[j] = collection[j], collection[i]


def __partition(collection: list, left: int, right: int) -> int:
    pivot = collection[right]
    smallIndex: int = left - 1
    for i in range(left, right):
        if (collection[i].compareTo(pivot)):
            smallIndex += 1
            __swap(collection, smallIndex, i)
    __swap(collection, smallIndex + 1, right)

    return smallIndex + 1


def __heapify(collection: list, length: int, i: int) -> None:
    left: int = 2 * i
    right: int = 2 * i + 1
    largest: int = i

    if (left < length) and (collection[largest].compareTo(collection[left])):
        largest = left

    if(right < length) and (collection[largest].compareTo(collection[right])):
        largest = right

    if(largest != i):
        __swap(collection, i, largest)
        __heapify(collection, length, largest)


def __buildHeap(collection: list) -> None:
    for i in range(math.floor(len(collection) / 2), -1, -1):
        __heapify(collection, len(collection), i)


def heapsort(collection: list) -> None:
    __buildHeap(collection)
    for i in range(len(collection) - 1, -1, -1):
        __swap(collection, 0, i)
        __heapify(collection, i, 0)


def introsort(collection: list) -> None:
    n: int = len(collection)
    depthLimit: int = math.log(n, 2)
    pivot = n-1

    if n < 2:
        return
    if pivot > depthLimit:
        heapsort(collection)
        return

    introsort(collection[0:pivot], depthLimit - 1)
    introsort(collection[pivot+1:n], depthLimit - 1)


def isSorted(collection: list, ascending: bool = True) -> bool:
    if ascending:
        return all(collection[i].compareTo(collection[i+1]) for i in range(len(collection)-1))
    else:
        return all(collection[i+1].compareTo(collection[i]) for i in range(len(collection)-1))


##################################### UNIT LIB TEST #####################################
def execute_test():
    pass


# Para testes unitários
if __name__ == '__main__':
    execute_test()
