# #region listes

# print("1. Liste - Modifiable, ordonnée, doublons autorisés")
# liste = list()
# liste = [10, 20, 30, 40]
# print(liste)

# # Ajouter un élément à la fin
# liste.append(50)
# print(liste)

# # Modifier l'élément 30 par 99
# liste[2] = 99
# print(liste)

# # Insérer l'élément  100 après 99
# liste.insert(3, 100)
# print(liste)

# # Trier par ordre croissant
# liste.sort()
# print("Liste triée ==>", liste)

# # Récupérer le premier/dernier élément de la liste
# print(liste[0])
# print(liste[-1])


#endregion

#region tuples

# print("2. Immuable, une fois la collection déterminée ont ne peut plus changer les valeurs")

# mon_tuple = tuple()
# mon_tuple = (100, 200, 300, 400)

# # impossible de changer la valeur
# #mon_tuple[1] = 999 # retourne une erreur

# #Déballage - récupérer les variables dans une collection en 4 variables différentes
# a, b, c, d = mon_tuple
# print ("déballage :", a, b, c, d, sep="\n- ")


#endregion

# #region set

# print("3. Pas de duplicata, éléments uniques et non ordonnés")
# mon_set = set()
# mon_set = {5, 10, 15 ,20}
# mon_set2 = {5, 10, 99 ,20}

# print("Différences mon_set/mon_set2:", mon_set.difference(mon_set2))
# # Indique ce qui n'est pas présent dans le set entre parenthèses

# # Ajouter un élément
# mon_set.add(25) # .append ne fonctionne pas

# # Supprimer un élément depuis sa valeur
# mon_set2.remove(99)
# print(mon_set2)

# mon_set.discard(58) # Supprime un élément seulement s'il existe --> ne lève pas d'erreur

# # Vérifier la présence d'un élément dans une collection
# print("15 est il présent dans le set : " 15 in)

# #endregion

#region dictionnaire
print("4. Dictionnaires - Clé => valeur")

personne = {
    "prenom" : "Nicolas",
    "age": 26,
    "ville":"Bruxelles"
}

print(personne)

# Modifier un des éléments du dictionnaire
personne["prenom"] = "Toto"
personne["salaire annuel"] =  int(50000)



print("\n élément supprimé du dictionnaire :", personne.pop("ville"), "\n----------------------------\n") #supprime un élément du dictionnaire

for cle, valeur in personne.items():
    print(f"-{cle} ==> {valeur}")

#endregion

