'''Merge Sort is a divide and conquer sorting algorithm.
It works by dividing the list into smaller parts, sorting each part, 
and then merging them back together in order.'''

#code for merge sort

def merge(array, s, m, l):
    L = [0] * (m - s + 1)
    R = [0] * (l - m)

    for i in range(len(L)):
        L[i] = array[s + i]

    for j in range(len(R)):
        R[j] = array[m + 1 + j]

    k = s
    i = 0
    j = 0
 # Loop 1: compare L[i] and R[j]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
# Loop 2: copy remaining elements of L
    while i < len(L) and j >= len(R):
        array[k] = L[i]
        k += 1
        i += 1
# Loop 3: copy remaining elements of R
    while i < len(L) and j < len(R):
        array[k] = R[j]
        k += 1
        j += 1


def merge_sort(array, s, l):
    if s < l:
        m = (s + l) // 2
        merge_sort(array, s, m)
        merge_sort(array, m + 1, l)
        merge(array, s, m, l)


# Example run
arr = [12, 11, 13, 5, 6, 7, 2]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
