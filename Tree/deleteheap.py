class DeleteHeap:
    def __init__(self):
        self.arr = []
        self.n = 0 
    
    def delete(self, data):
        i = 0
        self.arr[i] = self.arr[self.n - 1]
        self.n = self.n - 1

        while i <= self.n:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left <= self.n and self.arr[left] > self.arr[largest]:
                largest = left

            if right <= self.n and self.arr[right] >= self.arr[largest]:
                largest = right

            if largest == i:
                break
            else:
                temp = self.arr[i]
                self.arr[i] = self.arr[largest]
                self.arr[largest] = temp
                i = largest
