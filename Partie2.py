class binaryTree :

    def __init__(self, root):
        self.__root = root
        # root est un node sans ancestor

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        if self.__root == node :
            return True
        else :
            return False

    def size(self, node):
        if node.getRight() == None and node.getLeft() == None :
            return +0
        elif node.getRight() != None and node.getLeft() != None :
            return self.size(node.getRight()) + self.size(node.getLeft()) + 2
        elif node.getRight() != None :
            return self.size(node.getRight()) + 1
        elif node.getLeft() != None :
            return self.size(node.getLeft()) + 1

    def printValues(self, node):
        return
    def sumValues(self, node):
        return
    def numberLeaves(self, node):
        return
    def numberInternalNodes(self, node):
        return
    def height(self, node):
        return
    def belongs(self, node, val):
        return
    def ancestors(self, node, val):
        return
    def descendants(self, node, val):
        return
