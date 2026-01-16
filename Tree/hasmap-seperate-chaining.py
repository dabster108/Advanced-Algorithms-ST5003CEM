class HashMap:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]  

    def hash_function(self, key):
        return key % self.size  

    def put(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value   
                return

        self.table[index].append([key, value])  

    def get(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])
