# Créez un dictionnaire contenant les prix de quelques fruits tels que la pomme, la banane et l'orange. Demandez à
# l'utilisateur de saisir le nom d'un fruit, puis affichez le prix correspondant à ce fruit s'il existe dans le dictionnaire.

fruits = {
    'pomme' : 5,
    'banane' : 2.5,
    'poire' : 3,
    'orange' : 2
}

demande = input("Pour quel fruit souhaitez vous connaître le prix? \n Choix possibles : pomme, banane, poire, orange\n" )
if demande in fruits:
    print(fruits.get(demande), "€")