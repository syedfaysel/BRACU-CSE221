# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:43:23 2022

@author: rajo0
"""

def  bubbleSort(arr):
    
    for i in range(len(arr)-1):
        
        for j in range(len(arr)-i-1):
            
            if arr[j] > arr[j+1]:
                # swap 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                

a = [5,4,3,2,1]
bubbleSort(a)

print(a)