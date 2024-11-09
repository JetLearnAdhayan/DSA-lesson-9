class Node:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.data = v
    
def preorder(root):
    if root:  #if the root node is available then only continue
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data) 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)







root=Node(100)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(70)
root.right.right = Node(400)
root.right.left = Node(90)

print("Proeder Traversal")
preorder(root)

print("Postorder Traversal")
postorder(root)

print("Inorder Traversal")
inorder(root)