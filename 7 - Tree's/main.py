#!/usr/bin/env python3


class Node:
    def __init__(self,value,right=None,left=None):
        self.value = value
        self.right = right
        self.left  = left
        
class Tree:
    def __init__(self):
        self.deep = 0
    def chain(self,parent,right,left):
        parent.right = right
        parent.left  = left
    def inorder(self,parent:Node=None):
        if parent==None:return
        self.inorder(parent.right)
        print(parent.value)
        self.inorder(parent.left)
        
    def search(self,parent:Node,value):
        if parent == None :
            return
        if parent.value == value:
            print(f"{value} Found in deepth {self.deep}")
            return
        else:
            self.deep += 1
            self.search(parent.right,value)
            self.search(parent.left,value)
            
        
        
        
root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
t = Tree()
t.chain(root,n2,n5)
t.chain(n2,n3,n4)
t.chain(n5,n6,n7)
t.chain(n7,n8,n9)

t.inorder(root)
t.search(root,60)    
    