class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1 

class AVLTree:
    def __init__(self):
        self.root = None
    

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def createBST(self, root, data):
        if self.root == None:
            root = Node(data)
        if  data <root.data:
            root.left = self.createBST(root.left,data)
        elif data > root.data:
            root.right = self.createBST(root.right,data)
        else:
            return root 
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balancefactor = self.getBalance(root)

        #left -> left case 
        if balancefactor >1 and data < root.left.data:
            pass 
        
        # left -> right case 
        if balancefactor >1 and data > root.left.data:
            pass 
        
        # right -> right case 
        if balancefactor < -1 and data > root.right.data:
            pass 

        # right - > left case 
        if balancefactor <-1 and data < root.right.data:


            


 

    



 


