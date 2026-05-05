#Créez un programme qui génère un nombre aléatoire (import random) et permet à l'utilisateur de deviner ce nombre.
#Utilisez des correspondances pour comparer la devinette de l'utilisateur avec le nombre généré et fournir des indices.

taille = int(input("Quelle taille faites-vous (en cm)? \n "))
poids = int(input("Quel poids faites-vous (en kg) ? \n"))

imc = (poids / (taille/10)**2) * 100

match imc:
    case _ if 18 <= imc <= 25:
        print("Vous avez une corpulence normale")
    case _ if imc > 25:
        print("Vous êtes en surpoids")
    case _ if imc < 18:
        print("Vous êtes en sous-poids")