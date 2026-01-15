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

    
    def rightRotation(self,y):
        x = y.left 
        t2 = x.right 
        x.right = y 
        y.left = t2 
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        x.height = 1+max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def leftRotation(self,x):
        y = x.right 
        t2 = y.left 
        y.left = x 
        x.right = t2 
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y



    
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
            #ll
            return self.rightRotation(root)
        
        # left -> right case 
        if balancefactor >1 and data > root.left.data:
            #lr 
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        
        # right -> right case 
        if balancefactor < -1 and data > root.right.data:
            #rr
            return self.leftRotation(root)

        # right - > left case 
        if balancefactor <-1 and data < root.right.data:
            #rl
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)

        return root 


            


 

    



 


# get height get balance no needed 
# left and right rotation should be shown there 
