class Heapify:
    def __init__(self):
        self.arr = []
        self.n = 0 
    
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left <= n and arr[left] > arr[largest]:
            largest = left

        if right <= n and arr[right] >= arr[largest]:
            largest = right

        if largest != i:
            temp = arr[i]
            arr[i] = arr[largest]
            arr[largest] = temp
            return largest
        else:
            return i
