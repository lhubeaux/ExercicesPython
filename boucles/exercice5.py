# Gestionnaire de commandes de café amélioré :Écrivez un programme interactif qui prend les commandes de café en
# fonction des options telles que la taille, le type de café et les extras. Utilisez une boucle pour permettre à l'utilisateur
# de passer plusieurs commandes et affichez le prix total à la fin de chaque commande. Demandez ensuite à l'utilisateur
# s'il souhaite passer une autre commande et répétez le processus jusqu'à ce qu'il n'en ait plus envie.


commande = True
prix = 0
while commande:
    taille = int(input("Voulez vous un grand ou un petit café? \n 1. Grand 2. Petit :\n"))
    type_cafe = int(input("Quelle origine de café souhaitez-vous? \n 1. Kenya 2. Brésil 3. Nicaragua \n"))
    extras = int(input("Souhaitez vous du lait ou du sucre? \n 1. Lait 2. Sucre 3. Les deux \n"))
    match taille, type_cafe, extras:
        case 1, 1, 1:
            print("Voici votre grand café du Kenya avec du lait")
        case 1, 1, 2:
            print("Voici votre grand café du Kenya avec du sucre")
        case 1, 1, 3:
            print("Voici votre grand café du Kenya avec du lait et du sucre")
        case 1, 2, 1:
            print("Voici votre grand café du Brésil avec du lait")
        case 1, 2, 2:
            print("Voici votre grand café du Kenya avec du sucre")
        case 1, 2 ,3:
            print("Voici votre grand café du Kenya avec du lait et du sucre")
        case 1, 3, 1:
            print("Voici votre grand café du Nicaragua avec du lait")
        case 1, 3, 2:
            print("Voici votre grand café du Nicaragua avec du sucre")
        case 1, 3, 3:
            print("Voici votre grand café du Nicaragua avec du lait et du sucre")
        case 2, 1, 1:
            print("Voici votre petit café du Kenya avec du lait")
        case 2, 1, 2:
            print("Voici votre petit café du Kenya avec du sucre")
        case 2, 1 ,3:
            print("Voici votre petit café du Kenya avec du lait et du sucre")
        case 2, 2, 1:
            print("Voici votre petit café du Brésil avec du lait")
        case 2, 2, 2:
            print("Voici votre petit café du Brésil avec du sucre")
        case 2, 2, 3:
            print("Voici votre petit café du Brésil avec du lait et du sucre")
        case 2, 3, 1:
            print("Voici votre petit café du Nicaragua avec du lait")
        case 2, 3, 2:
            print("Voici votre petit café du Nicaragua avec du sucre")
        case 2, 3, 3:
            print("Voici votre petit café du Nicaragua avec du lait et du sucre")
        case _:
            print("Sélection invalide")
    prix = prix + 2
    print(f"Le total de votre commande est {prix}€")
    commande = input("Voulez-vous un autre café?\n 1. Oui 2. Non\n") == "1"
    if commande == False:
        print(f"Merci pour votre commande! Le total est de {prix}€.")