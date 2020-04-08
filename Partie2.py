class binaryTree :

    def __init__(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        if self.__root == node :
            return True
        else :
            return False
