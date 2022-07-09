#!/usr/bin/env python3



class Node:
    def __init__(self,item,back=None,head=None):
        self.item   = item
        self.head   = head
        self.back   = back


class LinkedList:
    def __init__(self,item=None):
        self.items = None if item==None else Node(item)
        
    def insert(self,value,index):
        item = Node(value)
        indx = 0
        p = self.items
        while p!=None:
            if index==indx:
                p.head.back,item.head = item.head,p.head.back
                p.head,item.back = item.back,p.head
                break
            p=p.head
            indx+=1
        
    def append(self,item):
        if self.items==None:
            self.items = Node(item)
            return
        p = self.items
        while p.head != None:
            p = p.head
        item = Node(item)   
        p.head = item    
        item.back = p
        
    def delete(self,value):
        if self.items==None:
            return
        if self.items.item == value:
            self.items = self.items.head
            self.items.head.back = None
            return
        p = self.items.head
        q = self.items
        while p != None:
            if p.item==value:
                q.head = p.head
                break
            q = p
            p = p.head
        
    def size(self):
        count = 0
        p = self.items
        while p!= None:
            count+=1
            p = p.head
        return count 
    
    def at(self,value):
        index = 0
        p = self.items
        while p!=None:
            if p.item == value:
                break 
            index+=1
        return index
            
    def print(self):
        p = self.items
        while p!=None:
            print(p.item)
            p = p.head
            
            
l = LinkedList(1)
l.append(2)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.delete(4)
l.delete(5)

l.print()
