"""
File: dna.py
Assignment: Lab
Language: Python 3
Author: Ayobami Adewale<aea8506@rit.edu>
Purpose: Functions to modified and test DNA LinkNode
"""

import linked_code


def convert_to_nodes(dna):
    """
    This function converts a string of DNA into a LinkNode
    :param dna: string version of a dna
    :return: A LinkNode version of the DNA
    """
    if dna == "":
        return None
    return linked_code.LinkNode(dna[0], convert_to_nodes(dna[1:]))


def convert_to_string(dna):
    """
    Takes in a LinkNode DNA and converts it to the string version.
    It does that by recursively return the dna value from the LinkNode.
    :param dna: LinkNode version of DNA
    :return: String version of DNA
    """
    if dna is None:
        # raise ValueError("Invalid dna")
        return ""
    elif dna.rest is None:
        return dna.value
    else:
        return dna.value + convert_to_string(dna.rest)


def is_match(dna1, dna2):
    """
    Takes in two DNA LinkNode and checks if the values of the dnas
     are the same.
    :param dna1: the first dna to be compared
    :param dna2: the second dna to be compared
    :return: True or False
    """
    if dna1 is None and dna2 is None:
        return True
    elif dna1 is None and dna2 is not None:
        return False
    elif dna1 is not None and dna2 is None:
        return False
    elif (dna1.rest is None) and (dna2.rest is None):
        if dna1.value == dna2.value:
            return True
        return False
    elif dna1.value != dna2.value:
        return False
    return is_match(dna1.rest, dna2.rest)


def is_pairing(dna1, dna2):
    """
    This function checks two DNAs for matching pairs
    :param dna1: The first dna node to be compared
    :param dna2: The Second dna node to be compared
    :return: True or False
    """
    if (dna1 is None) and (dna2 is None):
        return True
    elif (dna1 is None and dna2 is not None) or (dna2 is None and dna1 is not None):
        return False
    elif linked_code.length_iter(dna1) == linked_code.length_iter(dna2):
        if dna1.value == "A" and dna2.value == "T":
            pass
        elif dna1.value == "T" and dna2.value == "A":
            pass
        elif dna1.value == "C" and dna2.value == "G":
            pass
        elif dna1.value == "G" and dna2.value == "C":
            pass
        else:
            return False

    return is_pairing(dna1.rest, dna2.rest)


def is_palindrome(dna):
    """
    Checks if a DNA is a palindrome
    :param dna: The LinkNode version of DNA
    :return: True or False
    """

    if dna is None:
        return True
    length = linked_code.length_rec(dna) - 1
    if dna.value == linked_code.value_at(dna, length):
        if (dna.rest is None) or length == 2:
            return True
        new_dna = linked_code.remove_at(length, dna)
        return is_palindrome(new_dna.rest)
    else:
        return False


def substitution(dna, idx, base):
    """
    Substitutes single bases for others in the given DNA sequence.
    :param dna: The sequence in which the substitution mutation occurs
    :param idx: the index at which the substitution occurs
    :param base: the new base to be substituted at te specified index.
    :return: a new modified LinkNode
    """
    if dna is None:
        raise IndexError("invalid substitution index")

    if idx == 0:
        new = linked_code.remove_at(idx, dna)
        return linked_code.insert_at(idx, base, new)
    else:
        return linked_code.LinkNode(dna.value, substitution(dna.rest, idx - 1, base))


def insertion(lst1, lst2, idx):
    """
    Inserts DNA LinkNode #2 at a specific index of DNA LinkNode #1
    :param lst1: The DNA to be modified.
    :param lst2: The DNA to be inserted
    :param idx: The index where the second dna should be inserted
    :return:
    """
    if idx == 0:
        return linked_code.concatenate(lst2, lst1)
    elif lst1 is None:
        raise IndexError("Index out of bounds in insertion")
    else:
        return linked_code.LinkNode(lst1.value, insertion(lst1.rest, lst2, idx - 1))


def deletion(dna, idx, size):
    """
    This function deletes a specific segment from a LinkNode DNA
    :param dna: The DNA that will be deleted from
    :param idx: the index at which deletion begins
    :param size: The number of elements to be deleted
    :return:
    """
    if size == 0:
        return dna
    elif (idx + size) > linked_code.length_rec(dna):
        raise IndexError("invalid")
    elif dna is None:
        return None

    if idx == 0 < size:
        new_dna = linked_code.remove_at(idx, dna)
        return deletion(new_dna, idx, size - 1)
    else:
        return linked_code.LinkNode(dna.value, deletion(dna.rest, idx - 1, size))


def duplication(dna, idx, size):
    """
    Duplicates a part of a DNA starting from a given idx
    and it checks duplicating until the size has been reached
    :param dna: the sequence from which a segment will be copied.
    :param idx: the index for which the duplication starts
    :param size: the length of elements to be duplicated.
    :return:
    """
    if size == 0:
        return dna
    elif (idx + size) > linked_code.length_rec(dna):
        raise IndexError("invalid")
    elif dna is None:
        return None

    if -size < idx and idx <= 0:
        new = linked_code.insert_at(size, dna.value, dna)
        return linked_code.LinkNode(new.value, duplication(new.rest, idx - 1, size))
    else:
        return linked_code.LinkNode(dna.value, duplication(dna.rest, idx - 1, size))
