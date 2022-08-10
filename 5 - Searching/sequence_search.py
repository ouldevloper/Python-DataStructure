#!/usr/bin/env python3


from array import array


def search(array,value):
    l = len(array)
    
    for i in range(l):
        if value==array[i]:
            return i
    return -1


array = [1,3,5,32,5,7,43,6,8,45,7,8,5,6,6,8,5]
print(search(array,32))