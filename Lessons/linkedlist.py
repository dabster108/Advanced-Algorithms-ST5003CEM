class Node:
    def __init__ (self, data):
        self.data = None
        self.next = None
         
class linkedlist:
    def __init__ (self):
        self.head = None
        self.tail = None
    
    def addNode (self, data):
        newnode = Node (data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:  
            self.tail.next = newnode
            self.tail = newnode
            # current = self.head
            # while (current.next):
            #     current = current.next
            # current.next = newnode
    
    def print (self):
        current = self.head
        while (current!= None):
            print (current.data)
            current = current.next