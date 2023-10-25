#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Linked list  

class Node:
    """
    Class for creating Nodes of singly linked list
    contains data and next attributes.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    '''
    Provides basic Linked List implementation creation, insertion, updation, deletion, search and display. 
    '''

    def __init__(self) -> None:
        '''Initializes empty Linked list.'''
        self.head = None
        self.count = 0

    def insert(self, data, index: int = 0) -> None:
        '''Insert new node at specified index if not specified inserts at head of Linked list.'''
        if index < 0 or index >= self.count:
            print("Invalid Index.")
            return

        node = Node(data)
        self.count += 1
        if index == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head
        prev = None
        position = 0
        while current and position != index:
            position += 1
            prev = current
            current = current.next

        if prev:
            prev.next = node

        node.next = current
        return

    def insert_at_last(self, data) -> None:
        '''Insert new node at end of Linked list.'''
        current = self.head
        node = Node(data)
        self.count += 1

        if not current:
            self.head = node
            return

        while current.next:
            current = current.next
        current.next = node

    def remove_first(self) -> None:
        '''Removes first node from Linked list.'''
        if self.head:
            self.head = self.head.next
            count -= 1

    def remove_last(self) -> None:
        '''Removes last node from Linked list.'''
        if not self.head:
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next

        if current.next:
            current.next = None
        else:
            self.head.next = None
        count -= 1

    def remove_at(self, index: int) -> None:
        '''Removes node at specified index'''
        if index < 0 or index >= self.count:
            print("Invalid Index.")
            return

        if index == 0:
            self.remove_first()
            return

        current = self.head
        prev = None
        position = 0
        while current and position != index:
            position += 1
            prev = current
            current = current.next

        if prev and current:
            prev.next = current.next
        else:
            prev.next = None
        count -= 1

    def remove_item(self, data) -> bool:
        '''removes first occurance of matching data,
        returns True if data is found and removed else False'''
        if not self.head:
            print("No data in Linked List.")
            return False

        current = self.head
        if current.data == data:
            self.head = self.head.next
            self.count -= 1
            return True

        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            return False

        current.next = current.next.next
        count -= 1
        return True

    def search_item(self, data) -> Node:
        '''returns node with matching data if found else returns None'''
        if not self.head:
            print("No data in Linked List.")
            return None

        current = self.head

        while current:
            if current.data == data:
                return current
            current = current.next

        return None

    def update(self, data, new_data) -> bool:
        '''Updates first occurance of data and returns True if successful
        else return False if no matching data is found.'''
        node = self.search_item(data)
        if not node:
            return False

        node.data = new_data
        return True

    def display_list(self) -> None:
        '''Prints all items present in Linked list.'''
        current = self.head
        while current:
            print(f"{current.data}", end=" ->")
            current = current.next
        print("None")
