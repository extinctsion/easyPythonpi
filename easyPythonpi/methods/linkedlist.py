#!/usr/bin/env python
#-*- coding: utf-8 -*-


#Linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def create_node(data:'int')->'Node':
    a=Node(data)
    return a


# to link a node with another node
def node_link(a:'Node', b:'Node'):
    a.next=b
    b.next=None
    #a=node(data1)


# to count number of nodes
def count_node(head:'Node')->'int':
    count=0
    if head is None:
        return count
    else:
        temp=head
        while(temp!=None):
            count=count+1
            temp=temp.next
    return count

# to diplay a linked list whose header node is passed as an argument.
def display_nodes(head:'Node')->None:
    t=head
    while t is not None:
        print(t.data,"->",end="")
        t=t.next
    print("NULL")

# re revrese a lined list
def revrese_lined_list(head: 'Node')->'Node':
    prev = None
    # a -> b -> c -> d -> e -> f -> g -> h -> None
    current = head
    while current is not None:
        next = current.next # b -> c -> d -> so one...

        current.next = prev # a -> None
        prev = current # b -> a -> None
        current = next # c -> d -> e -> f -> g -> h -> None
    head=prev # h -> g -> f -> e -> d -> c -> b -> a -> None

    return head