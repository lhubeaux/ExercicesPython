# Générez une liste de 10 nombres aléatoires compris entre 1 et 50. Affichez cette liste générée. Ensuite, filtrez les
# nombres pairs de la liste et créez une nouvelle liste ne contenant que ces nombres pairs. Enfin, affichez la nouvelle
# liste contenant uniquement les nombres pairs.
import random
liste=[]
for i in range (1,10,1):
    liste.append(random.randint(1,50))
print(liste)
liste2 = []
for j in range(0,len(liste),1):
    if liste[j] % 2 == 0:
        liste2.append(liste[j])
    else:
        pass
print(liste2)