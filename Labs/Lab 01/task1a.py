# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:48:21 2022

@author: 21101078
"""



# Open a file
with open("input1a.txt", 'r') as file:
    # line = file.readline()
    # print(line)
    
    tc = int(file.readline())
    with open("output1a.txt",'w') as file_out:
        
        for i in range(tc):
            
            num =int(file.readline())
            # print(num)
            
            if num%2 ==0:
                file_out.write(f"{num} is an even number.\n")
            else:
                file_out.write(f"{num} is a odd number.\n")






# writing to file
# with open("output1a.txt", 'w') as file_out:
#     file_out.write("Writing\n")
#     file_out.write("Writing")
    
#     line = file_out.readline()
#     print(line)