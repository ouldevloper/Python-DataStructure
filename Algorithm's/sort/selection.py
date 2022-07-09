#!/usr/bin/env python3
# Selection Sort

class Array:
    
    def __init__(self,items=[]):
        self.items = items
        
    def sort(self):
        l = len(self.items)
        for row in range(l):
            min_ = row
            for line in range(row,l):
                if self.items[line] < self.items[min_]:
                    min_ = line
            self.items[row],self.items[min_] = self.items[min_],self.items[row]
    
    def append(self,value):
        self.items.append(value)
    
    def print(self):
        print(self.items)

arr = [1,5,7,3,6,8,9,56,8,4,6,3,5,7,1,5,3,7,3]

a = Array(arr)
a.sort()
a.print()