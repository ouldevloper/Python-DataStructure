#!/usr/bin/env pytho3


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self,value=None):
        self.items = Node(value) if value != None else None
        self.back  = self.items
        self.front = self.items
        
    def dequeue(self):
        if self.front != None:
            item = self.front.value
            self.items = self.items.next
            self.front = self.items  
        return item
    
    def enqueue(self,value):
        item = Node(value)
        p = self.items
        while p.next!=None:
            p=p.next
        p.next = item
        self.back = p.next
       
        
    def size(self):
        count = 0
        p = self.items
        while p!=None:
            count+=1
            p=p.next
        return count
    
    def getBack(self):
        return self.back.value if self.back!=None else None
    def getFront(self):
        return self.front.value if self.front!=None else None
    
    def print(self):
        p = self.items
        while p!=None:
            print(p.value)
            p = p.next
        

q = Queue(0)
q.enqueue(4)
q.enqueue(2)
q.enqueue(12)
q.enqueue(13)
q.print()
print('----------------')
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print('---------------')
q.print()
print('--------------')
print(q.getBack())
print(q.getFront())
print(q.size())

#n1 = Node(1)
#n2 = Node(2)
#n3 = Node(3)
#n4 = Node(4)