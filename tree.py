class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

# Example usage
if __name__ == '__main__':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("In-order Traversal: ", end='')
    inorder_traversal(root)
    print("\nPre-order Traversal: ", end='')
    preorder_traversal(root)
    print("\nPost-order Traversal: ", end='')
    postorder_traversal(root)