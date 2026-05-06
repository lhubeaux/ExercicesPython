# Écrivez un programme qui demande à l'utilisateur d'entrer un mot. Utilisez une boucle pour afficher chaque caractère
# du mot un par un jusqu'à la fin du mot.

mot = input("Veuillez entrer votre mot: \n")
for i in mot:
    print(i, end=' ')