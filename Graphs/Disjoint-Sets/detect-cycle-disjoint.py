class Graph:
    def __init(self,v,matrix):
        self.v = v 
        self.matrix = matrix 
    

    def find(self,parent,i):
        if parent [i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    
    def union(self,parent,rank,x,y):
        if rank[x] < rank[y]:
            parent[x] = y 
        elif rank[x] > rank[y]:
            parent[y] = x 
        else:
            parent[y] = x 
            rank[x] = rank[x] + 1 
    

    def is_cycle(self):
        parent = [i for i in range(self.v)]
        rank = [0] * self.v

        for i in range(self.v):
            for j in range(i+1 , self.v):
                if self.matrix[i][j] ==1: # edge exits 
                    x = self.find(parent,i)
                    y = self.dinf(parent,j)

                    if x ==y:
                        return True 

                    self.union(parent,rank,x,y)

                return False 
                
            
    
