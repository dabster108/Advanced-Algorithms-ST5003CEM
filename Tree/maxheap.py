class MaxHeap:
    def __init__(self):
        self.arr = []   
        self.n = 0      

    def maxheap(self, data):
        self.arr.append(data)
        i = self.n        
        self.n += 1       

        while i > 0:
            p = (i - 1) // 2  
            if self.arr[i] > self.arr[p]:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
                i = p
            else:
                break  

    def display(self):
        print(self.arr)


# Example usage
heap = MaxHeap()
heap.maxheap(10)
heap.maxheap(20)
heap.maxheap(5)
heap.maxheap(30)
heap.display()  
