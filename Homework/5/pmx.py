# -*- coding: utf-8 -*-

"""
Implementación del algoritmo PMX en python
"""

__author__ = 'Gustavo Gómez M.'
__email__ = "ggomez91@gmail.com"

import random

def _repeated(element, collection):
    c = 0
    for e in collection:
        if e == element:
            c += 1
    return c > 1

def _swap(data_a, data_b, cross_points):
    c1, c2 = cross_points
    new_a = data_a[:c1] + data_b[c1:c2] + data_a[c2:]
    new_b = data_b[:c1] + data_a[c1:c2] + data_b[c2:]
    return new_a, new_b


def _map(swapped, cross_points):
    n = len(swapped[0])
    c1, c2 = cross_points
    s1, s2 = swapped
    map_ = s1[c1:c2], s2[c1:c2]
    for i_chromosome in range(n):
        if not c1 < i_chromosome < c2:
            for i_son in range(2):
                while _repeated(swapped[i_son][i_chromosome], swapped[i_son]):
                    map_index = map_[i_son].index(swapped[i_son][i_chromosome])
                    swapped[i_son][i_chromosome] = map_[1-i_son][map_index]
    return s1, s2


def pmx(parent_a, parent_b):
    assert(len(parent_a) == len(parent_b))
    n = len(parent_a)
    cross_points = [4,7]
    swapped = _swap(parent_a, parent_b, cross_points)
    mapped = _map(swapped, cross_points)

    return mapped

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9]
    b = [3,8,9,4,5,6,7,1,2]
    off = pmx(a, b)
    print(off)
