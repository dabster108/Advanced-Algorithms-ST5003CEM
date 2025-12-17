class queue:
    def __init__(self, capacity):
        self.q = [0] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        
        def isFull (self):
            return self.rear == self.capacity - 1 

        def isEmpty(self):
            return self.front == -1 and self.rear == -1 
        
        def enqueue (self, data):
            if (self.isFull()):
                print ("Queue is Full")
            else:
                if (self.front == -1 and self.rear == -1):
                    self.front = 0
                    self.rear = 0
                    self.q [self.rear] = data
                else:
                    self.rear = self.rear + 1
                    self.q [self.rear] = data 
                    
        def dequeue (self):
            if (self.isEmpty()):
                print ("Queue is Empty")
                return -1
            else:
                if (self.front == self.rear):
                    tmp = self.q [self.front]
                    self.front = -1
                    self.rear = -1
                    return tmp
            else:
                tmp = self.q [self.front]
                self.front = self.front + 1
                return tmp