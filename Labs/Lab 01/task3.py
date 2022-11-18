
#  Bubble sort modification for best case complexity - order of n


with open("input3.txt", 'r') as file_in:

    n = int(file_in.readline())
    arr = file_in.readline()
    arr = list(map(int, arr.split()))

    def bubbleSort(arr):
        
        # checking if the array is already sorted
        
        is_sorted = True
        for i in range(len(arr)-1):
            
            if arr[i]>arr[i+1]:
                is_sorted = False
                break
            
        if (is_sorted == True):
            # if the array is already sorted,
            # no need to execute the actual sorting part
            # Hence it turns only n times
            return
        
        else:
            # if given array is not sorted, it need to be sorted
            
            for i in range(len(arr)-1):
                
                for j in range(len(arr)-i-1):
                    
                    if arr[j]> arr[j+1]:
                        
                        # swap
                        arr[j], arr[j+1] = arr[j+1], arr[j]


    bubbleSort(arr) # Function call
    
    with open("output3.txt", "w") as file_out:
        for i in arr:
            file_out.write(f"{i} ")

                    

