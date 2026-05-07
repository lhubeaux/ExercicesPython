# Créez une liste de mots contenant des doublons. Transformez ensuite cette liste en un ensemble pour éliminer les
# doublons. Affichez l'ensemble résultant

liste = ['voiture', 'maison', 'lit', 'voiture', 'train', 'lit']

liste.sort()
unique_liste = []
for item in liste:
    if item not in unique_liste:
        unique_liste.append(item)
print(unique_liste)

unique = set(liste)
print(unique)
#créer un set direct bcp plus simple