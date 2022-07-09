#!/usr/bin/env python3

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self,value=None):
        self.__items = None if value ==None else Node(value)
        self.head = None
    
    def insert(self,value):
        if self.__items == None:
            self.__items = Node(value,self.__items)
            self.head = self.__items
            return
        self.head.next = Node(value,self.__items)
        self.head.next.next = self.__items
        self.head = self.head.next
        
    def delete(self):
        pass
         
    def print(self):
        p = self.__items
        while p != self.head:
            print(p.value)
            p = p.next

l = LinkedList()
l.insert(2)
l.insert(2)

l.print()
exit()
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)

l.print()
            
            