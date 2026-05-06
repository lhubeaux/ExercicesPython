# Jeu de devinette de nombre amélioré : Écrivez un jeu interactif où l'ordinateur génère un nombre aléatoire entre 1 et
# 100, et l'utilisateur doit deviner ce nombre. Utilisez une boucle pour permettre à l'utilisateur de faire plusieurs
# tentatives. Après chaque tentative, demandez à l'utilisateur s'il souhaite continuer à jouer. Répétez le processus
# jusqu'à ce qu'il décide de ne plus jouer. Enfin, affichez le nombre de tentatives utilisées pour deviner le nombre.

import random
nombre_a_deviner = random.randint(1,10)
guess = 0

while nombre_a_deviner != guess:
    guess = int(input("Devinez le chiffre (1-10):\n"))
    match guess:
        case _ if guess == nombre_a_deviner:
            print("Vous avez trouvé!")
        case _ if guess > nombre_a_deviner:
            print("Le nombre à deviner est plus petit")
        case _ if guess < nombre_a_deviner:
            print("Le nombre à deviner est plus grand")
        case _ if guess > 10 or guess < 1:
            print("Valeur incompatible")
    