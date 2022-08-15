#!/usr/bin/env python3 


from curses import noecho


class Node:
    def __init__(self,value=None,right=None,lift=None):
        self.item = value 
        self.right = right 
        self.lift  = lift 
    def set_right(self,right):
        self.right=right
    
    def set_lift(self,lift):
        self.lift = lift
        
        
#                          10
#                 5                  11                         
#               6   8          12          15                                
#              7      9     13    14    16    19                       
#                                             20                      
#                                                                   

root = Node(10)


n1 = Node(5)
n2 = Node(6)
n3 = Node(8)
n4 = Node(7)
n5 = Node(9)
n6 = Node(11)
n7 = Node(12)
n13 = Node(13)
n8 = Node(14)
n9 = Node(15)
n10 = Node(16)
n11 = Node(19)
n12 = Node(20)

root.lift = n6
root.right = n1
n1.right = n2
n1.lift = n3
n2.right = n4
n3.right = n5

n6.right = n7
n6.lift = n9
n7.right = n13
n7.lift = n8
n9.right = n10
n9.lift = n11
n11.right=n12


def preorder(root):
    if root==None:
        return
    print(root.item)
    preorder(root.right)
    preorder(root.lift)
    
preorder(root)