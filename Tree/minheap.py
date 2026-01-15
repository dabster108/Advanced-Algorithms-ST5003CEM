class MinHeap:
    def __init__(self):
        self.arr = []  
        self.n = 0     

    def minheap(self, data):
        self.arr.append(data)
        i = self.n       
        self.n += 1       
        while i > 0:
            p = (i - 1) // 2  
            if self.arr[i] < self.arr[p]: 
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
                i = p
            else:
                break  

    def display(self):
        print(self.arr)



heap = MinHeap()
heap.minheap(10)
heap.minheap(20)
heap.minheap(5)
heap.minheap(30)
heap.display()  
