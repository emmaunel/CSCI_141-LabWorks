"""
File: select_median.py
Assignment: Lab
Language: Python 3
Author: Ayobami Adewale<aea8506@rit.edu>
Purpose: Calculate and print the optimal location for a store and the sum
    of the distances that people would have to travel to reach the store from each
    given location using quick select.
"""

import time


def median(lis):
    """
       Finds the medium of a list of unsorted list
       :param lis: list of the store location(unsorted)
       :return: the medium
    """
    if len(lis) % 2 == 0:
        lower = quick_select(lis, ((len(lis) // 2) - 1))
        upper = quick_select(lis, (len(lis) // 2))
        return (upper + lower) / 2
    else:
        return quick_select(lis, len(lis) // 2)


def quick_select(lis, k):
    """
        Takes a list of unsorted number and finds the k'th smallest number.
        It creates two list(small and large) and sets them based on a pivot value.
        if the lenght of the small list is less than or equal to k and k is less than
        the lenght of the small plus the occurences of the pivot, then it returns than pivot.
        If not, it recursively calls itself
        :param lis: an unsorted list
        :param k: smallest number in the list
        :return: smallest number in the list
    """
    if len(lis) == 0:
        return
    else:
        pivot = lis[len(lis) // 2]
        small_list = []
        large_list = []
        count = 0

        for e in lis:
            if e == pivot:
                count += 1
            elif e > pivot:
                large_list.append(e)
            else:
                small_list.append(e)

        m = len(small_list)

        if k >= m and k < (m + count):
            return pivot
        elif m > k:
            return quick_select(small_list, k)
        else:
            return quick_select(large_list, k - m - count)


def distance_sum(lst, best_location):
    """
    Given an unsorted list and the best location, this function adds up all the
    other location from the best location.
    :param lst: unsorted list
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
