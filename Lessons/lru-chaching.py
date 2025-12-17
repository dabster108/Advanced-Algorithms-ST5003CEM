class Node:
    def __init__ (self, key, value):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key
        
class LRUCaching:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.dummyhead = Node (0)
        self.dummytail = Node (0)
        self.map = {}
        
    def put (self, key, value):
        if key in self.map.key:
            node = self.map.get(key)
            self.remove (node)
            
        elif (len (self.map)== self.capacity):
            # remove least recently used (tail)
            self.remove (self.dummytail.prev)
            pass
        
        newnode = Node (key, value)
        self.insert (newnode)
        
    def get (self, key):
        node = self.map.get (key)
        if node == None:
            return -1
        self.remove (node)
        self.insert (node)
        return node.value
        
    def insert (self, newnode):
        self.map [newnode.key] = newnode
        if (self.dummyhead.next == None):
            self.dummyhead.next = newnode
            newnode.prev = self.dummyhead
            newnode.next = self.dummytail
            self.dummytail.prev = newnode
        
        else:
            newnode.next = self.dummyhead.next
            self.dummyhead.next.prev = newnode
            newnode.next = self.dummyhead
            self.dummyhead.next = newnode
            
        def remove (self, node):
            self.map.pop (node.key):
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None