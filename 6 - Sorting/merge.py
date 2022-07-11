#!/usr/bin/env python3

class Array:
    def __init__(self,item1=[],item2=[]):
        self.items1 = item1
        self.items2 = item2
        self.res = []
    
    
    def Merge(self):

        n = len(self.items1)
        m = len(self.items2)        
        i = j = 0

        while i<n and j< m:
            if self.items1[i] < self.items2[j]:
                self.res.append(self.items1[i])
                i += 1
            else:
                self.res.append(self.items2[j])
                j += 1
        while i<n:
            self.res.append(self.items1[i])
            i += 1
        while j<m:
            self.res.append(self.items2[j])
            j+=1
    
        
    def print(self):
        print(self.res)
    
print("Algorithm Merge")
arr1 = [1,3,9]
arr2 = [2,4,7,98]
a = Array(arr1,arr2)
a.Merge()

a.print()