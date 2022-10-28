
# Practice Quick sort
def partition(L, low, high):

    pivot = L[high] 

    i = low - 1
    for j in range(low,high):
        if L[j]<L[high]:
            i+=1
            L[j], L[i] = L[i], L[j]

    L[i+1], L[high] = L[high], L[i+1]
    return i+1


def quick_sort(L, low, high):

    if low>=high:
        return 

    p = partition(L, low, high)
    quick_sort(L,low, p-1)
    quick_sort(L, p+1, high)


if __name__ == "__main__":
    A = [2,1,1,0,3]

    quick_sort(A,0, len(A)-1)
    print(A)