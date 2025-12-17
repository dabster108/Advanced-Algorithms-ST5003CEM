#Queue - Enqueue , Dequeue , IsEmpty , Size
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0]*capacity
        self.front = -1 
        self.rear = -1

    def isFull(self):
        return self.rear == self.capacity - 1
    
    def isEmpty(self):
        return self.front == -1 and self.rear == -1
    
    def enqueue(self,data):
        if self.isFull():
            print("Queue is full cannot insert the element")
        else:
            if(self.front ==-1 and self.rear == -1):
                self.front = self.rear = 0
                self.queue[self.rear] = data
            else:
                self.rear = self.rear + 1 
                self.queue[self.rear] = data
    

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty cannot dequeue element")
            return -1
        else:
            # do deque front and rer represents the same element 
            # after dequeuing the element make front and rear -1
           if(self.front == self.rear):
               temp = self.queue[self.front]
               self.front = self.rear = -1
               return temp
           else:
               temp = self.queue[self.front]
               self.front = self.front + 1
               return temp

Queue = Queue(5)
Queue.enqueue(10)
Queue.enqueue(20)
Queue.enqueue(30)
print(Queue.dequeue())  # Output: 10
print(Queue.dequeue())  # Output: 20



# Write an algorithm to implment a stack using two queues
# Write an algorithm to implement a queue using two stacks