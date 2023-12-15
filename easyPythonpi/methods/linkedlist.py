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

# get length of list
def get_linked_list_length(head:'node')->'int':
    
    # base case
    if head is None:
        return 0

    length, curr = 1, head
    # loop through list to accumulate length
    while head.next:
        head = head.next
        length += 1
    
    return length

# given the head of a linked list and a number n, rotate the linked list by n spaces
def rotate_linked_list(head:'node', n:int)->'list':

    # if linked list is None or length of 1 or n is negative
    # just return head
    if head is None or head.next is None or n <= 0:
        return head
    
    # get length of list
    length = get_linked_list_length(head)

    # get new tail
    tail = head
    while tail.next:
        tail = tail.next

    # optimize rotation to account for looping through entire list multiple times
    n = n % length

    # if n == 0, we don't need to rotate anything
    if n == 0:
        return head

    curr = head
    for i in range(length - n - 1):
        curr = curr.next
    
    # update necessary pointers
    new_head = curr.next
    curr.next = None
    tail.next = head

    return new_head