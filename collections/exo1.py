# Commencez par créer une liste de 10 nombres aléatoires compris entre 1 et 100. Ensuite, affichez cette liste générée.
# Après cela, calculez la somme de tous les éléments de la liste et affichez-la.
import random
liste=[]
for i in range (1,10,1):
    liste.append(random.randint(1,100))
print(liste)

add = 0
for j in range(0,9,1):
    add = add + liste[j]
print("Tous les nombres de la liste valent :", add)