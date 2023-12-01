#!/usr/bin/python3
"""Find peak algorithm."""

def find_peak(list_of_integers):
    """ Finds the peak in a list_of_integers """

    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    gm = int(length / 2)
    li = list_of_integers

    if gm - 1 < 0 and gm + 1 >= length:
        return li[gm]
    elif gm - 1 < 0:
        return li[gm] if li[gm] > li[gm + 1] else li[gm + 1]
    elif gm + 1 >= length:
        return li[gm] if li[gm] > li[gm - 1] else li[gm - 1]

    if li[gm - 1] < li[gm] > li[gm + 1]:
        return li[gm]

    if li[gm + 1] > li[gm - 1]:
        return find_peak(li[gm:])
    return find_peak(li[:gm])
