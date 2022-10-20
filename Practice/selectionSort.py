# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 00:03:27 2022

@author: rajo0
"""


def selection_sort(arr):
    
    for i in range(len(arr)):
        
        min = arr[i]
        min_idx = i
        for j in range(i+1, len(arr)):
            
            if arr[j]<min:
                min = arr[j]
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
arr = [10, 9, 5, 3]
selection_sort(arr)

print(arr)