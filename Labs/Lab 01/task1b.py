# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:25:02 2022

@author: 21101078
"""

# Task 1b

with open("input1b.txt", 'r') as file_in:
    
    with open("output1b.txt", 'w') as file_out:
        
        tc = int(file_in.readline())
        
        
        for i in range(tc):
            
            line = str(file_in.readline())
            line = line[len("calculate")+1:len(line)-1]
            # print(line)
            
            a, o, b = line.split(' ')
            
            a, b = int(a), int(b)
            
            
            if (o == "+"):
                file_out.write(f"The result of {a} {o} {b} is {a+b}\n")
                
            elif (o == "-"):
                file_out.write(f"The result of {a} {o} {b} is {a-b}\n")
                
            elif (o == "*"):
                file_out.write(f"The result of {a} {o} {b} is {a*b}\n")
                
            else:
                file_out.write(f"The result of {a} {o} {b} is {a/b}\n")
            