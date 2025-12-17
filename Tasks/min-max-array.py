def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2
    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)

    return min(left_min, right_min), max(left_max, right_max)


arr = [5, 2, 8, 1, 9, 3]
mn, mx = find_min_max(arr, 0, len(arr)-1)
print("Minimum:", mn)
print("Maximum:", mx)
 