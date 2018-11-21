"""
File: select_median.py
Assignment: Lab
Language: Python 3
Author: Ayobami Adewale<aea8506@rit.edu>
Purpose: Calculate and print the optimal location for a store and the sum
    of the distances that people would have to travel to reach the store from each
    given location using quick sort algorithm.
"""

import time


def quick_sort(L):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        (less, same, more) = partition(pivot, L)
        return quick_sort(less) + same + quick_sort(more)


def partition(pivot, L):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    (less, same, more) = ([], [], [])
    for e in L:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return less, same, more


def median(l):
    """
    Finds the medium of a list of sorted list
    :param lis: list of the store location(sorted)
    :return: the meium
    """
    l = quick_sort(l)
    if len(l) == 1:
        return l[0]

    if len(l) % 2 == 1:
        return l[(len(l)) // 2]
    else:
        index1 = len(l) // 2
        index2 = index1 - 1
        return (l[index1] + l[index2]) / 2


def distance_sum(lst, best_location):
    """
       Given an sorted list and the best location, this function adds up all the
       other location from the best location.
       :param lst: sorted list
       :param best_location: given to us from median function
       :return: total sum
    """
    total = 0
    for e in lst:
        if best_location >= e:
            total += (best_location - e)
        else:
            total += (e - best_location)

    return total


def main():
    """
    Takes in a data file and file the numbers in the file.
    With that list of number, it finds the optimum location
    and them find the sum of the other distance from the optimum location.
    It also uses time function to see how quick it finds the optimum location.
    :return:
    """
    file_name = input("Enter data file: ")
    lst = []
    f = open(file_name)

    for line in f:
        split = line.split()
        indes = split[1]
        lst.append(int(indes))

    start = time.time()
    optimum = median(lst)
    end = time.time()

    totalDistance = distance_sum(lst, optimum)

    print ("Optimum new store location: " + str(optimum))
    print ("Sum of distances to new store: " + str(totalDistance))
    print ('Elapsed time: ' + str(end - start))


main()
