def findk(A, low, high, k):

    # for valid k
    if k > 0 and k <= high - low + 1:

        p = partition_k(A, low, high)

        if p - low == k - 1:
            return A[p]

        elif p - low > k - 1:
            return findk(A, low, p - 1, k)

        else:
            return findk(A, p + 1, high, k - p + low - 1)

    else:
        return "Invalid index"


def partition_k(A, low, high):

    pivot = A[high] #considering the last item as pivot

    i = low - 1
    for j in range(low, high):
        if A[j] < pivot:
            i = i + 1
            (A[i], A[j]) = (A[j], A[i])

    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1



# ================================
arr2 = [1, 3, 4, 5, 9, 10, 10]
print(findk(arr2, 0, len(arr2)-1, k=5))
print(findk(arr2, 0, len(arr2)-1, k=2))
print(findk(arr2, 0, len(arr2)-1, k=7))