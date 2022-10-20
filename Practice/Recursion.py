# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:37:40 2022

@author: rajo0
"""

def recur(n):
    if (n==10):
        return(1)
    else:
        return(recur(n+1)+1)
    
    
print(recur(0))


def fact(n):
    if n<=0:
        return 1
    
    else: 
        return n*fact(n-1)
    
print(fact(4))