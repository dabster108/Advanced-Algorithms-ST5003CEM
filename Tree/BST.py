class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def createBST(self, root, data):
        if self.root == None:
            root = Node(data)
        if  data <root.data:
            root.left = self.createBST(root.left,data)
        elif data > root.data:
            root.right = self.createBST(root.right,data)
        else:
            return root 
        return root