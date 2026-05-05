# Créez un programme qui gère les commandes de café en fonction des différentes options telles que la taille, le type de café, les extras, etc.
# Utilisez des correspondances pour traiter chaque option et calculer le prix total de la commande

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
        print("Séleciton invalide")