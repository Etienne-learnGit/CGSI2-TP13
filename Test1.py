from Partie1 import *
from Partie2 import *

N21 = node(21, None, None)
N18 = node(18, None, None)
N3 = node(3, None, None)

N19 = node(19, N21, N18)
N4 = node(4, None, N3)
N6 = node(6, None, None)

N17 = node(17, N19, None)
N5 = node(5, N6, N4)

N12 = node(12, N17, N5)
Tree = binaryTree(N12)
Racine = Tree.getRoot()

#print( Tree.size(Racine) )
#print( Tree.printValues(Racine) )
#print( Tree.sumValues(Racine) )
#print( Tree.numberLeaves(Racine) )
#print( Tree.numberInternalNodes(Racine) )
#print( Tree.height(Racine) )
print( Tree.belongs(Racine, 6))
