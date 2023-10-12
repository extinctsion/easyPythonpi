#!/usr/bin/env python
#-*- coding: utf-8 -*-


#Linked list                   
                  
def create_node(data:'int')->'list':
    class node:
        def __init__(self,data):
            self.data=data
            self.next=None
    
    a=node(data)
    return a

# to link a node with another node
def node_link(a:'int',b:'int'):
    a.next=b
    b.next=None
    #a=node(data1)
          
         
# to count number of nodes                                  
def count_node(head:'node')->'int':
    if head is None:
        return 0
    else:
        temp=head
        count=0
        while(temp!=None):
                count=count+1
                temp=temp.next
        return count   

# to diplay a linked list whose header node is passed as an argument.
def display_nodes(head:'node')->'int':
    t=head
    while t is not None:
        print(t.data,"->",end="")
        t=t.next
    print("NULL")

