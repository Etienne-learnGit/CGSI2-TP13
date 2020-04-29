class binaryTree :

    def __init__(self, root):
        self.__root = root
        # root est un node sans ancestor

    def getRoot(self):
        return self.__root

    def isRoot(self, node): #qui vérifie si node est la racine de l'arbre
        if self.__root == node :
            return True
        else :
            return False

    def size(self, node): #retourne la taille de l'arbre, le nombre de nodes
        if node is None :
            return + 0
        else :
            return self.size(node.getRight()) + self.size(node.getLeft()) + 1

    def printValues(self, node): #affiche toute les valeurs des nodes de l'arbre
        if node is None :
            return ""
        else :
            return str(node.getVal()) +" "+ self.printValues(node.getRight()) + self.printValues(node.getLeft())

    def sumValues(self, node): #retourne la somme des valeurs de chaques nodes
        if node is None :
            return 0
        else :
            return self.sumValues(node.getRight()) + self.sumValues(node.getLeft()) + node.getVal()

    def numberLeaves(self, node): #retourne le nombre de feuilles
        if node is None :
            return + 0
        if node.getLeft() is None and node.getRight() is None:
            return + 1
        else :
            return self.numberLeaves(node.getLeft()) + self.numberLeaves(node.getRight())

    def numberInternalNodes(self, node): #retourne le nombre de node interne
        return self.size(node)-self.numberLeaves(node)

    def height(self, node): #retourne la hauteur de l'arbre
        if node is None:
            return - 1
        else :
            return max(self.height(node.getRight()), self.height(node.getLeft())) + 1

    def belongs(self, node, val): #qui vérifie si val est une des valeurs d'un noeud de l'arbre
        if node is None:
            return False
        if node.getVal() == val:
            return True
        else:
            return self.belongs(node.getLeft(), val) or self.belongs(node.getRight(), val)

    def ancestors(self, node, val): #qui affiche les antécédents d'un arbre
        return
    def descendants(self, node, val): #qui affiche les descendants d'un arbre
        return
