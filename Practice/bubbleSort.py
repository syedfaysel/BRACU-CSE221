

def  bubbleSort(arr):
    
    for i in range(len(arr)-1):
        
        for j in range(len(arr)-i-1):
            
            if arr[j] > arr[j+1]:
                # swap 
                arr[j], arr[j+1] = arr[j+1], arr[j]  
                

a = [2,1,1,0,1,0,7,8]
bubbleSort(a)

print(a)