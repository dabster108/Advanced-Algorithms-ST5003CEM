class TreeNode:
    def __init__(self,data):
        self.left  = None 
        self.right = None 
        self.data = data 


    def preorder(self,root):
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)




root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
