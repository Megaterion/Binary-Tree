class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if(node==None):
            self.root = TreeNode(value)
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value)

    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)

    def printPreorder(self, node):
        if (node!=None):
            print(node.data)
            self.printPreorder(node.left)
            self.printPreorder(node.right)
    def printPostorder(self, node):
        if(node!=None):
            self.printPostorder(node.left)
            self.printPostorder(node.right)
            print(node.data)

def test():
    T = Tree()
    T.addNode(T.root, 200)
    T.addNode(T.root, 300)
    T.addNode(T.root, 100)
    T.addNode(T.root, 30)
    print("Inorder")
    T.printInorder(T.root)
    print("Preorder")
    T.printPreorder(T.root)
    print("Postorder")
    T.printPostorder(T.root)
