# Créez une fonction nombres_pairs_impairs() qui prend une liste de nombres en entrée et retourne deux listes
# distinctes, l'une contenant les nombres pairs et l'autre les nombres impairs.
import random

def nombres_pairs_impairs(liste_nbres):
    liste_pairs = []
    liste_impairs = []
    for i in liste_nbres:
        if i % 2 == 0:
            liste_pairs.append(i)
        else:
            liste_impairs.append(i)
    return liste_pairs, liste_impairs

nombres = []
for j in range (0, 10, 1):
    nombres.append(random.randint(0, 100))
print(nombres)
pairs, impairs = nombres_pairs_impairs(nombres)
print(f"Nombre pairs : {pairs}")
print(f"Nombre impairs : {impairs}")
