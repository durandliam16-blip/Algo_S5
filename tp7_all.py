##TP7 - Ex1 et 2
##voir photo pour dessin graphe d'ex et representation des matrices et listes d'adjacences

#Q1
"""Complexité en espace de la matrice d'adjacence est par n**2 avec n=|V|=la taille de la matrice.
    Mais liste[i] (listes d'adjacences) est de complexité d'espace de cst car liste.
    Ainsi, les listes d'adjacences sont plus optimale dans l'utilisation des ressources."""

#Q2
"""
Type représentation | Recherche de voisins | Ajout d'arête | Suppr d'arête | Test d'adja entre 2 sommets
--------------------|----------------------|---------------|---------------|---------------------------
Liste d'adjacence   |   O(k)               | O(1)          | O(k)          | O(k)
Matrice d'adja      |   O(n)               | O(1)          | O(1)          | O(1)
"""

#sym si matrice orienté
#autant de 1 que d'aretes si pas symetrique

#test dadja entre 2 sommetes via 2 dicos
#se poser les bonnes questions sur représentation
#listes adja en tant que dico

import numpy as np
mat_test=np.array([[0,1,1,0,0,0],
            [0,0,1,1,0,0],  
            [0,0,0,1,1,0],
            [0,0,0,0,1,1],
            [0,0,0,0,0,1],
            [0,0,0,0,0,0]])

#si matrice non orienté
def est_symetrique(M):
    return np.array_equal(M, M.T)
B=np.array([[0,1,1,0],
            [1,0,1,1],
            [1,1,0,1],
            [0,1,1,0]]) 
print(est_symetrique(B))
