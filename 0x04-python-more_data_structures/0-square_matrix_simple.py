#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    big_nest = []
    for x in matrix:
        small_nest = []
        for y in x:
            small_nest.append(y**2)
        big_nest.append(small_nest)
    return big_nest
