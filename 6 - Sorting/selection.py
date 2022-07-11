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

print("Algorithm Selection")
arr = [1,5,3,6,8,4,7,5,78,4,8,4,8,4,3,6,4,5,43,5,43,5,43,6,43,45,43,43,45,4,45,43,45,43,45,43,45,43,45,43,5,43,
       6,7,76,87,8,76,65,45,43,65,98,987,87,76,65,45,45,65,76,8,87,76,6,65,76,87,87,87,76,65,6,75,8,9,98,87,65,
       76,8,76,6,456,1,5,3,6,8,4,7,5,78,4,8,4,8,4,3,6,4,5,43,5,43,5,43,6,43,45,43,43,45,4,45,43,45,43,45,43,45,
       43,45,43,5,43,6,7,76,87,8,76,65,45,43,65,98,987,87,76,65,45,45,65,76,8,87,76,6,65,76,87,87,87,76,65,6,75,
       8,9,98,87,65,76,8,76,6,456,76,87,8,76,65,45,43,65,98,987,87,76,65,45,45,65,76,8,87,76,6,65,76,87,87,87,76
       ,65,6,75,8,9,98,87,65,45,6345,6435,62,623,5234,523,4245,6432,6523,653,4623,4623,632,632,6326,346,23,3245,
       76,8,76,6,456,1,5,3,6,8,4,7,5,78,4,8,4,8,4,3,6,4,5,43,5,43,5,43,6,43,45,43,43,45,4,45,43,45,43,45,43,45,
       43,45,43,5,43,345,56,347,3473,457,34,734,734,573,47,34,76,75,675,67,456,75,673,4673,68,36,83658,356,37,3567]
a = Array(arr)
a.sort()
a.append(0)
a.sort()
a.print()