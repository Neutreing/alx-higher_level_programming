#!usr/bin/python3

def search_replace(my_list, search, replace):
    z = my_list.copy()
    for i in z:
        if i == search:
            z[z.index(search)] = replace
    return z
