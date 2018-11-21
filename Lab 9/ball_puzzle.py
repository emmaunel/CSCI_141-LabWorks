"""
File: ball_puzzle.py
Assignment: Lab
Language: Python 3
Author: Ayobami Adewale<aea8506@rit.edu>
Purpose: Sorts certain color balls in their respective can
"""

from ball_puzzle_animate import *
from stack import *

can_list = [make_empty_stack(), make_empty_stack(), make_empty_stack()]


def moveOne(from_can, to_can):
    """
    The fuunction removes the top of the can and
    pushes it to the desired can
    :param from_can: The can you want to remove from
    :param to_can: The can you want to move to
    :return:
    """
    item = top(from_can)
    from_can = pop(from_can)
    to_can = push(to_can, item)
    return to_can, from_can


def solve2(stack_list):
    """
    This function takes in a stack_list and sort
    the balls in their right can using this algorithm.

    Algorithm:
    While the Red can is not empty(stack_list[0]),
    check if the top value is Blue. If it is, move the blue
    ball to the blue can(stack_list[2]) and if it is not,
    move the rest of the ball to the green can(stack_list[1]).

    After that check if the Green can is empty, if not, move
    all the red ball to the red can and all the green ball to the
    blue can.

    Lastly, check if the top of the blue is green, if it is, it is
    moved to the green can.
    :param stack_list: A list of stack that represent cans
    :return: The number of steps it took to sort the balls
    """
    count = 0
    while not is_empty(stack_list[0]):
        if top(stack_list[0]) == 'B':
            moveOne(can_list[0], can_list[2])
            animate_move(stack_list, 0, 2)
            count += 1
        else:
            moveOne(can_list[0], can_list[1])
            animate_move(stack_list, 0, 1)

    while not is_empty(stack_list[1]):
        if top(stack_list[1]) == 'R':
            moveOne(can_list[1], can_list[0])
            animate_move(stack_list, 1, 0)
            count += 1
        else:
            moveOne(can_list[1], can_list[2])
            animate_move(stack_list, 1, 2)

    if is_empty(can_list[2]):
        pass
    else:
        while top(stack_list[2]) != 'B':
            moveOne(stack_list[2], stack_list[1])
            animate_move(stack_list, 2, 1)
            count += 1
    return count


def main():
    """
    Takes input from the user and add each character to the
    first empty stack in a list.
    :return: The number of moves it takes to solve the puzzle
    """
    color = input("Enter the initial balls in the red can: ")
    animate_init(color)
    for i in color:
        push(can_list[0], i)
    moves = solve2(can_list)
    print("It took " + str(moves) + " moves to solve the puzzle")
    print("Close the window to quit")
    animate_finish()


main()
