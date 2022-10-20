
#  Merge sort

def merge(arr, p,q,r):


    L = arr[:q+1]
    R = arr[q+1:]
    
    L.append(10**5)
    R.append(10**5)
    
    i = j = 0

    for k in range(len(arr)):
        if L[i]<= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
            
    
def merge_sort(arr,p,r):
    if p<r:
        q = p+(r-p)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p,q, r)
        

arr = [4,2,6,1,2]
print(arr)

merge_sort(arr,0, len(arr)-1)

print(arr)

    