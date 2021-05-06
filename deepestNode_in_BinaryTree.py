class new_Node:
    def __init__ (self, key):
        self.data = key
        self.left = self.right = None

def height(root):
    if(not root):
        return 0

    leftHt = height(root.left)
    rightHt = height(root.right)

    return max(leftHt, rightHt) + 1

def deepestNode(root, levels):
    if(not root):
        return

    if(levels == 1):
        print(root.data)
    elif(levels > 1):
        deepestNode(root.left, levels -1)
        deepestNode(root.right, levels -1)


if __name__ == '__main__':

    root = new_Node('a')
    root.left = new_Node('b')
    root.right = new_Node('c')
    root.left.left = new_Node('d')
   # root.right.left = new_Node(5)
   # root.right.right = new_Node(6)
   # root.right.left.right = new_Node(7)
   # root.right.right.right = new_Node(8)
   # root.right.left.right.left = new_Node(9)


    levels = height(root)

    deepestNode(root, levels)
    
