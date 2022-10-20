# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:16:09 2022

@author: rajo0

"""

# INSERTION SORT

def ins_sort(array):
    
    for j in range(1, len(array)):
        
        key = array[j]
        # Insert array[j] into the sorted sequence A[0...j-1]
        
        i = j-1
        while(i>=0 and array[i]>key):
            
            array[i+1] = array[i]   # Right shifting elements
            
            i = i-1
        
        array[i+1] = key  # putting a[j] or key in the right place
        
        
arr = [3]
print(arr)
ins_sort(arr)
print(arr)        
    
