# Task 02: All test cases passed
# Merge Sort

# Merge two list into one :
    
def merge(A, B):
    merged_list = []
    
    len_a , len_b = len(A), len(B)
    index_a, index_b = 0, 0
    
    while (index_a < len_a and index_b < len_b):
        
        if A[index_a] < B[index_b]:
            merged_list.append(A[index_a])
            index_a += 1

        else:
            merged_list.append(B[index_b])
            index_b += 1
            
    # check if all elements are added or not from both sub list
    if index_a < len_a:
        merged_list.extend(A[index_a:])
        
    elif index_b < len_b:
        merged_list.extend(B[index_b:])
            
        
    # now all the elements are  added & both lists are merged 
    return merged_list


# complexity of merge function is O(n)

def merge_sort(A):
    
    if len(A) <=1:
        return A
    
    mid = len(A)//2
    Left = merge_sort(A[:mid])
    Right = merge_sort(A[mid:])
    
    return merge(Left, Right)

#========================================

with open("input2.txt", 'r') as file_in:

    n = file_in.readline()
    arr = file_in.readline()
    arr = [int(x) for x in arr.split()]
    
    arr = merge_sort(arr)
    
    # writing to output
    with open("output2.txt", 'w') as file_out:
        for i in arr:
            file_out.write(f"{i} ")
        file_out.write("\n")
