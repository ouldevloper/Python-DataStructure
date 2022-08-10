#!/usr/bin/env python3


from array import array
from xml.dom import HierarchyRequestErr


def search_recursion(array,value,low,high):
    if high>=low:
        index = (low+high)//2;
        print(index)
        if array[index]==value:
            return index
        elif array[index]> value:
            return search_recursion(array,value,low,index-1)
        else:
            return search_recursion(array,value,index+1,high)
    else:
        return -1
    

def search_loops(array,value,low,high):
    while high>=low:
        index = (low+high)//2;
        if array[index]==value:
            return index
        elif array[index]> value:
            high = index-1
        else:
            low = index+1
    else:
        return -1
array=[1,5,3,6,8,10,16,54,76,98]
print(search_loops(array,98,0,len(array)-1))