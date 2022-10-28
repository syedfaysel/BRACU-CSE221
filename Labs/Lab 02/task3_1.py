# Task 03_1 : Quick Sort


def quick_sort(A, low, high):
    
    if low >= high:
        return
    
    p = partition(A, low, high)
    
    quick_sort(A, low, p-1)
    quick_sort(A, p+1, high)



def partition(A, low, high):
    
    pivot = A[high] #considering the last item as pivot
    
    i = low-1
    for j in range(low, high):
        if A[j] < pivot:
            i+=1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[high] = A[high], A[i+1]
    return i+1


# ==========================
arr  = [5,-1,10,2,8]
print(arr)

quick_sort(arr, 0, len(arr)-1)

print(arr)