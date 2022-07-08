#!/usr/bin/env python3

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self,value=None):
        if value!=None:
            self.linkedlist = Node(value=value)
        else: self.linkedlist = None
    def print(self):
        p = self.linkedlist
        while p!=None:
            print(p.value)
            p = p.next

    def append(self,value=None):
        item = Node(value)
        if self.linkedlist == None:
            self.linkedlist = item
            return
        if item!=None:
            p = self.linkedlist
            while p.next!=None:
                p=p.next
            p.next = item
    def remove(self,value):
        head = self.linkedlist
        next = self.linkedlist.next
        Found = False
        if self.linkedlist.value == value:
            self.linkedlist = self.linkedlist.next
            return
        while next!=None and not Found:
            if next.value == value:
                Found = True
                break
            head=next
            next=next.next
        if Found:
            head.next = next if next==None else next.next
    def remove_at(self,index):
        if index == 0:
            self.linkedlist = self.linkedlist.next
            return
        head = self.linkedlist
        next = self.linkedlist.next
        idx = 0
        while next!=None:
            if idx == index:
                head.next = next if next==None else next.next
                break
            head=next
            next=next.next
            idx += 1
        
    def get_at(self,index):
        head = self.linkedlist
        ret = None
        idx = 0
        while head!=None:
            if index==idx:
                ret = head.value
                break
            idx += 1
            head = head.next
        return ret
    
    def index(self,value):
        idx = 0
        head = self.linkedlist
        while head!=None:
            if head.value == value:
                break
            head = head.next
            idx += 1
        return idx
    
    
           

l = LinkedList(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(7)


l.remove_at(2)
l.print()

print(l.get_at(43))


