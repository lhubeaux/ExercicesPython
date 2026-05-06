# Écrivez un programme qui demande à l'utilisateur d'entrer un mot. Utilisez une boucle pour inverser l'ordre des lettres
# du mot et affichez le mot inversé à la fin.

mot = input("Veuillez entrer mot : ")
for i in range(len(mot) -1, -1, -1):
    print(mot[i], end='')