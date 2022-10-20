
#  Merge sort

def merge(arr, p,q,r):
    # n1 = q-p+1
    # n2 = r-q
    
    # L = [0]*n1
    # R = [0]*n2
    
    q = len(arr)//2
    L = [:q]
    R = [q:]
    
    
    # for i in range(n1):
    #     L[i] = arr[p+i]
    
    # for j in range(n2):
    #     R[j] = arr[q+j+1]
    
    
    
    i = j = k = 0

    
    while(i<len(L) and j<len(R)):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        
        else:
            arr[k] = R[j]
            j+=1
        k+=1
        
    
    # while(i<len(L)):
    #     arr[k] = L[i]
    #     i+=1
    #     k+=1
        
    # while(j<len(R)):
    #     arr[k] = R[j]
    #     j+=1
    #     k+=1
        
        
        

arr = [4,5,6,1]

merge(arr)

print(arr)

    