#!/usr/bin/env python
#-*- coding: utf-8 -*-

# To bubble sort and array or list
def sort(list:'list'):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
