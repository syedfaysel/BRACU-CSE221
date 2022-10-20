# Quick Sort


def partition(L, low, high):

    pivot = L[high]

    i = low - 1  # i initially pointed to -1
    for j in range(low, high):
        if L[j]<pivot:
            # when L[j] is less than pivot, first increase i by 1 (i+=1), 
            # then swap L[j], with L[i]
            i+=1
            L[i],L[j] = L[j],L[i]
        
    # place pivot at it's right position and swap
    L[i+1], L[high] = L[high], L[i+1]
    # end of this part, all the elements in the left part are less than pivot and right side elements are larger than pivot

    return i+1



def quick_sort(L, low, high):

    if low>=high:
        return
    p = partition(L, low, high)

    # partition will return an index of the previous pivot. so, we got two parts to sort or partition again
    quick_sort(L,low,p-1)
    quick_sort(L, p+1, high)


if __name__== "__main__":
    L = [2,1,1,0,1,0,7,8]

    quick_sort(L,0,len(L)-1)
    print(L)