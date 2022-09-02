class Node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val

    #Creating an instance of the node class to construct the tree
    # Trees start leftmost node and move left, root, right
root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)



def inOrder(root):
    if root:
        (root.childleft)
        print (root.nodedata)
        inOrder(root.childright)
inOrder(root)