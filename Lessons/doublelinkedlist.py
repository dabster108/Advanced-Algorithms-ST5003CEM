class Node:
    def __init__ (self, key, value):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key
        
class LRUCaching:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.dummyhead = Node (0, 0)
        self.dummytail = Node (0, 0)
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead
        self.map = {}
        
    def put (self, key, value):
        if key in self.map:
            node = self.map.get(key)
            self.remove (node)
        
        if len (self.map) == self.capacity:
            # remove least recently used (tail)
            self.remove (self.dummytail.prev)
        
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
        # Insert after dummy head (most recently used)
        newnode.next = self.dummyhead.next
        self.dummyhead.next.prev = newnode
        newnode.prev = self.dummyhead
        self.dummyhead.next = newnode
            
    def remove (self, node):
        if node.key in self.map:
            self.map.pop (node.key)
        node.prev.next = node.next
        node.next.prev = node.prev