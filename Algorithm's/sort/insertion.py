#!/usr/bin/env python3





class Array:
    def __init__(self,item=[]):
        self.items = item
        
    def append(self,value):
        self.items.append(value)
        
    def sort(self):
        l = len(self.items)
        for row in range(l):
            for line in range(row,0,-1):
                if self.items[line]<self.items[line-1]:
                    self.items[line],self.items[line-1] = self.items[line-1],self.items[line]
    
    def print(self):
        print(self.items)
    
    
arr = [1,5,3,6,8,4,7,5,78,4,8,4,8,4,3,6,4]
a = Array(arr)
a.sort()
a.append(0)
a.sort()
a.print()