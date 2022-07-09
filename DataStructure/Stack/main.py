#!/usr/bin/env python3


class Node:
    def __init__(self,value=None,next=None):
        self.value  = value
        self.next   = next

class Stack:
    def __init__(self,value=None):
        self.items = None if value==None else Node(value)
        
    def pop(self):
        ret = None
        if self.items == None : return None
        if self.items.next == None :
            ret = self.items.value
            self.items = None
            return
        
        p = self.items
        while p.next.next != None:
            p = p.next
        ret = p.next.value
        p.next = None
        return ret
    
    def push(self,value):
        if self.items == None : 
            self.items = Node(value)
            return
        p = self.items
        while p.next != None:
            p = p.next
        p.next = Node(value)
    
    def print(self):
        p = self.items
        while p!=None:
            print(p.value)
            p = p.next
        
    
s =Stack(0)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.pop())
print('----------------')
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print('----------------')
s.print()