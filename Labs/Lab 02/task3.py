# Task 03 (i) : Quick Sort


def quick_sort(A, low, high):
    
    if low >= high:
        return
    
    p = partition(A, low, high)
    
    quick_sort(A, low, p-1)
    quick_sort(A, p+1, high)


# Partition Functin
def partition(A, low, high):
    
    pivot = A[high] #considering the last item as pivot
    
    i = low-1
    for j in range(low, high):
        if A[j] < pivot:
            i+=1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[high] = A[high], A[i+1]
    return i+1


# ============File I/O=============
with open("input3.txt", 'r') as file_in:

    n = file_in.readline()
    arr = file_in.readline()
    arr = [int(x) for x in arr.split()]
    
    quick_sort(arr, 0, len(arr)-1)
    
    # writing to output file
    with open("output3.txt", 'w') as file_out:
        for i in arr:
            file_out.write(f"{i} ")
        file_out.write("\n")


#=====================================
# Task 03 (ii) : findK()

def findk(A, low, high, k):

    # for valid k
    if k > 0 and k <= high - low + 1:

        p = partition(A, low, high)

        if p - low == k - 1:
            return A[p]

        elif p - low > k - 1:
            return findk(A, low, p - 1, k)

        else:
            return findk(A, p + 1, high, k - p + low - 1)

    else:
        return "Invalid K"


#========== Test cases ==========
arr2 = [1, 3, 4, 5, 9, 10, 10]
print(findk(arr2, 0, len(arr2)-1, k=5))
print(findk(arr2, 0, len(arr2)-1, k=2))
print(findk(arr2, 0, len(arr2)-1, k=7))