class MinimumSpanningTree:
    def __init__(self, v):
        self.parent = [-1] * v
        self.size = [0] * v
        self.mst = [-1] * v
    
    def Krushkal(self, edges):
        #Sort edges based on weight
        edges.sort(key=lambda x: x[2])
        edgetaken = 0
        edgecounter = 0
        while edgetaken < self.v :
            e = edges[edgecounter]
            edgecounter += 1
            u = e[0]
            v = e[1]
            w = e[2]
            uabsroot = self.find(u)
            vabsroot = self.find(v)
            if uabsroot == vabsroot:
                continue
            else:
                self.mst[u] = v
                #add u, v, w in matrix
                self.union(uabsroot, vabsroot)
    
    def find(self, u):
        if self.parent[u] == -1:
            return u
        return self.parent[u] == self.find(self.parent[u])
    
    def union(self, uabsroot, vabsroot):
        if self.size[uabsroot] > self.sizep[vabsroot]:
            self.parent[vabsroot] = uabsroot
        elif self.size[uabsroot] < self.size[vabsroot]:
            self.parent[uabsroot] = vabsroot
        else:
            self.parent[uabsroot] = vabsroot
            self.size[vabsroot] += 1
# edge = [(0,1,4), (0, 7, 8), and so on]