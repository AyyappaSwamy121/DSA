class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data,end=" ")
    inorder_traversal(root.right)

def preorder_traversal(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data,end=" ")

root = Node(10)
root.left = Node(17)
root.right = Node(18)
root.left.left = Node(11)
root.left.right = Node(99)
root.right.left = Node(16)
root.right.right = Node(77)
root.left.right.left = Node(1)
inorder_traversal(root)
print()
preorder_traversal(root)
print()
postorder_traversal(root)
