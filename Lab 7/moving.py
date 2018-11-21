"""
File: moving.py
Assignment: Lab
Language: Python 3
Author: Ayobami Adewale<aea8506@rit.edu>
Purpose: Using greedy algorithm to pack a bunch of items in a box
"""

from dataclasses import dataclass


@dataclass
class Box:
    capacity: int
    items: list
    capacity_left: int


@dataclass
class Items:
    name: str
    weight: int


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
        return quick_sort(more) + same + quick_sort(less)


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


def read_files(file_name):
    """
    Read a file and put the first line in boxes
    and the rest of the file in items
    :param file_name:
    :return:
    """
    file = open(file_name)
    weight = file.readline().split()
    boxes = []
    items = []
    for i in weight:
        boxes = boxes + [Box(int(i), [], int(i))]

    for line in file:
        cur_line = line.split()
        items += [Items(cur_line[0], int(cur_line[1]))]
    file.close()
    return boxes, items


def roomiest(file):
    """
    Sorts the item largest to smallest, sort the boxes by available weight
    Loops through the items and place item in the boxes.
    If the weight of an item is larger than the allocated space, it ignores it.
    :param file:
    :return:
    """
    boxes, items = read_files(file)
    items = sort_Items(items)
    for ele in items:
        index = find_remain(boxes)
        if ele.weight > boxes[index].capacity_left:
            pass
        else:
            boxes[index].items.append(ele)
            boxes[index].capacity_left = boxes[index].capacity_left - ele.weight

    return boxes, items



def find_remain(Boxes):
    """Find the index of the greatest remaining allowed weight"""
    index = 0
    bst_wwight = 0
    bst_index = 0
    for ele in Boxes:
        if ele.capacity_left > bst_wwight:
            bst_wwight = ele.capacity_left
            bst_index = index
            index += 1
        else:
            index += 1
    return bst_index


def tightest(file):
    """Sorts the item largest to smallest, sort the boxes by available weight
    Loops through the items and place item in the boxes.
    If the weight of an item is larger than the allocated space, it ignores it."""
    boxes, items = read_files(file)
    items = sort_Items(items)
    for ele in items:
        index = find_least(boxes, ele.weight)
        if index < 0:
            pass
        else:
            boxes[index].items.append(ele)
            boxes[index].capacity_left = boxes[index].capacity_left - ele.weight

    return boxes, items


def find_least(Boxes, weight):
    """
    Find the index of the least remaining allowed weight.
    :param Boxes:
    :param weight:
    :return:
    """
    low_left = 789
    current_ind = 0
    best_ind = -1
    for ele in Boxes:
        if weight <= ele.capacity_left < low_left:
            low_left = ele.capacity_left
            best_ind = current_ind
            current_ind += 1
        else:
            current_ind += 1
    return best_ind


def sort_Items(Items):
    """
    With the given unsorted items, it uses a temp list to check if an item list is sorted
    or not.
    :param Items:
    :return:
    """
    temp_list = []
    new_item = []
    states = []
    for items in Items:
        temp_list.append(int(items.weight))
    sorts = quick_sort(temp_list)
    for _ in range(0, len(Items)):
        states.append(0)
    for element in sorts:
        count = 0
        for stuff in Items:
            if element == stuff.weight and states[count] == 0:
                new_item = new_item + [stuff]
                states[count] = 1
            else:
                count += 1
    return new_item


def one_box(file):
    """Sorts the item largest to smallest, sort the boxes by available weight
       Loops through the items and place item in the boxes.
       If the weight of an item is larger than the allocated space, it ignores it."""
    boxes, items = read_files(file)
    items = sort_Items(items)
    states = []
    for _ in range(0, len(items)):
        states.append(0)

    for b in boxes:
        for index in range(0, len(items)):
            if items[index].weight <= b.capacity_left and states[index] == 0:
                b.items.append(items[index])
                b.capacity_left -= items[index].weight
                states[index] = 1
            else:
                pass

    return boxes, items

def print_statement(box, item, numeber):
    """Makes the results user friendly"""
    print("Results from Greedy strategy " + str(numeber))
    num = 1
    for i in box:
        print("Box " + str(num) + " of weight capacity " + str(i.capacity_left) + " contains:")
        for ite in range(0, len(i.items)):
            print(i.items[ite].name + " of weight " + str(i.items[ite].weight))
        num += 1
    print("\n")


def main():
    file = input("Enter data filename: ")
    box1, itme1 = roomiest(file)
    print_statement(box1, itme1, 1)
    box2, itme2 = tightest(file)
    print_statement(box2, itme2, 2)
    box3, itme3 = one_box(file)
    print_statement(box3, itme3, 3)

main()
