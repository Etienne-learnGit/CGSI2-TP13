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
        if node is None :
            return + 0
        else :
            return self.size(node.getRight()) + self.size(node.getLeft()) + 1

    def printValues(self, node):
        if node is None :
            return ""
        else :
            return str(node.getVal()) +" "+ self.printValues(node.getRight()) + self.printValues(node.getLeft())

    def sumValues(self, node):
        if node is None :
            return 0
        else :
            return self.sumValues(node.getRight()) + self.sumValues(node.getLeft()) + node.getVal()

    def numberLeaves(self, node):
        if (node.getLeft() == None) and (node.getRight() == None) :
            return + 1
        else :
            return self.numberLeaves(node.getRight()) + self.numberLeaves(node.getRight())

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
