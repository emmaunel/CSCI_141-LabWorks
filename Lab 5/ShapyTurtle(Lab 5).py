"""
File: shapy_turtle.py
Assignment: Homework
Language: Python 3
Author: Ayobami Adewale<aea8506@rit.edu>
Purpose: ShapyTurltle is an interpreter for a 'shorthand language'
that allows s to express turtle programs compactly as a string
"""


import turtle as t


def get_num(text):
    """
    This funciton takes in a string and checks if there is a number in front,
    if there is, it will return that number
    :param text: String that has mixture of number and characters
    :return: a number in front of a string
    """
    number = ""
    if not text[0].isdigit():
        "Come back"
        print ("Sorry, your command two character in front of a number")
        exit(1)
    while text != "" and text[0].isdigit():
        number += text[0]
        text = text[1:]
    if number == "":
        return None
    return number


def processSt(text):
    """
    This function takes a set of commands and
    determine the right funcion to execute
    based on the first letter
    :param text: set of commands for turtle
    :return: None
    """
    temp_text = text
    while text != "":
        ch = text[0]
        text = text[1:]
        if ch == '<':
            text = turn_left(text)

        elif ch == '>':
            text = turn_right(text)

        elif ch == 's' or ch == 'S':
            text = draw_square(text)

        elif ch == 't' or ch == 'T':
            text = draw_triangle(text)
        elif ch == 'c' or ch == 'C':
            text = draw_circle(text)
        elif ch == 'f' or ch == 'F':
            text = move_forward(text)
        elif ch == 'b' or ch == 'B':
            text = move_backward(text)
        elif ch == 'u' or ch == 'U':
            t.pu()
        elif ch == 'd' or ch == 'D':
            t.pd()
        elif ch == 'r' or ch == 'R':
            text = draw_rectangle(text)
        elif ch == 'p' or ch == 'P':
            text = draw_polygon(text)
        elif ch == 'g' or ch == 'G':
            text = goto_location(text)
        elif ch == 'z' or ch == 'Z':
            text = change_color(text)
        else:
            "Fix this"
            print ("Error. That command does not exist")
            print ("You tried to use this command " + temp_text)
            print ("Close the program to quit!!!")


def turn_left(text):
    """
    This function turn left based of the number in front of the received string.
    :param text: text with a number of degree in front
    :return: a sliced text of the original text
    """
    num = get_num(text)
    text = text[len(num):]
    num = int(num)
    t.left(num)
    return text


def turn_right(text):
    """
    This function turn right based of the number in front of the received string.
    :param text: text with a number of degree in front
    :return: a sliced text of the original text
    """
    num = get_num(text)
    text = text[len(num):]
    num = int(num)
    t.right(num)
    return text


def draw_square(text):
    """
    This function draws a square with the length of t
    he number in front of the received string.
    :param text: text with length number in front
    :return: a sliced text of the original text
    """
    num = get_num(text)
    text = text[len(num):]
    num = int(num)
    for i in range(4):
        t.fd(num)
        t.left(90)
    return text


def draw_triangle(text):
    """
    This function draws an equilateral triangle with the
    length of the number in front of the received string.
    :param text: text with length number in front
    :return: a sliced text of the original text
    """
    num = get_num(text)
    text = text[len(num):]
    num = int(num)
    for i in range(3):
        t.fd(num)
        t.left(120)
    return text


def draw_circle(text):
    """
    This function draws a circle with a radius given by the number
    in front of the string
    :param text: text with radius number in front
    :return: a sliced text of the original text
    """
    num = get_num(text)
    text = text[len(num):]
    num = int(num)
    t.circle(num)
    return text


def move_forward(text):
    """
    This function moves forward a certain amount based on the number
    in front of the string
    :param text: text with distance number in front
    :return: a sliced text of the original text
    """
    num = get_num(text)
    text = text[len(num):]
    num = int(num)
    t.fd(num)
    return text


def move_backward(text):
    """
    This function moves backward a certain amount based on the number
    in front of the string
    :param text: text with distance number in front
    :return: a sliced text of the original text
    """
    num = get_num(text)
    text = text[len(num):]
    num = int(num)
    t.bk(num)
    return text


def draw_rectangle(text):
    """
    This function a rectangle with a specific width and length which is
    received from the text. It also separates the two number to differentiate
    the length from the width.
    :param text: text that has two numbers for the length and the width
    :return: a sliced text of the original text
    """
    length = get_num(text)
    text = text[len(length):]
    if text[0] == ',':
        width = get_num(text[1:])

    t.fd(int(length))
    t.left(90)
    t.fd(int(width))
    t.left(90)
    t.fd(int(length))
    t.left(90)
    t.fd(int(width))
    t.left(90)
    return text


def draw_polygon(text):
    """
    This function a polygon with a specific angle and length which is
    received from the text. It also separates the two number to differentiate
    the length from the width.
    :param text: text that has two numbers for the length and the angle
    :return: a sliced text of the original text
    """
    side = get_num(text)
    text = text[len(side):]
    if text[0] == ',':
        length = text[1:]

    angle = 360 / int(side)

    for i in range(int(side)):
        t.fd(int(length))
        t.left(angle)
    return text


def goto_location(text):
    """
    This function goes to a specific location based on the numbers
    received from the text. It also separates the two number to differentiate
    the length from the width.
    :param text: text that has two numbers for the x and the y
    :return: a sliced text of the original text
    """
    x = get_num(text)
    text = text[len(x):]
    if text[0] == ',':
        y = get_num(text[1:])

    x = int(x)
    y = int(y)

    t.goto(x, y)
    return text


def change_color(text):
    """
    This function will change the turtle's pencolor based on the number
    received from the text.
    :param text: text that has a number that determine the pencolor
    :return: a sliced text of the original text
    """
    color = get_num(text)
    text = text[len(color):]
    color = int(color)

    if color == 0:
        t.pencolor("red")
    elif color == 1:
        t.pencolor("blue")
    elif color == 2:
        t.pencolor("green")
    elif color == 3:
        t.pencolor("yellow")
    elif color == 4:
        t.pencolor("brown")
    else:
        t.pencolor("black")
    return text


if __name__ == "__main__":
    commands = input("Enter your commands: ")
    processSt(commands)
    t.done()
