class node :

    def __init__(self, val, right, left):
        self.__val = val
        self.__right = right
        self.__left = left

    def getVal(self):
        return self.__val
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left

    def setRight(self, newRight):
        self.__right = newRight
    def setLeft(self, newLeft):
        self.__left = newLeft

    def __str__(self):
        return ('la valeur du noeud est : '+str(self.__val))
