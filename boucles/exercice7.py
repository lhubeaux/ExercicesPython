# Gestion des repas du jour améliorée : Développez un programme interactif qui permet à l'utilisateur de choisir un menu
# pour chaque repas de la journée parmi des options prédéfinies. Utilisez une boucle pour faciliter la saisie des choix
# pour chaque repas et affichez un résumé des choix de repas à la fin. Demandez ensuite à l'utilisateur s'il souhaite
# choisir les repas pour un autre jour. Répétez le processus jusqu'à ce qu'il décide de ne plus choisir de repas.


commande = True
jour = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
i=0
while commande:
    
    # Saisie utilisateur
    print(f"Choississez votre menu pour {jour[i]}!")
    dejeuner = int(input("Choisissez votre déjeuner: \n 1. Pain au chocolat 2. Croissant 3. Brioche \n (Les 3 sont accompagnés d'un café) : "))
    diner = int(input("Choisissez votre dîner: \n 1. Sandwich 2. Dürüm 3. Pastabox : "))
    souper = int(input("Choisissez votre souper: \n 1. Pâtes bolognaise 2. Steak frites 3. Saumon fumé : "))

    # Détermination des noms des plats
    # Déjeuner
    if dejeuner == 1:
        nom_dejeuner = "Pain au chocolat + café"
    elif dejeuner == 2:
        nom_dejeuner = "Croissant + café"
    elif dejeuner == 3:
        nom_dejeuner = "Brioche + café"
    else:
        nom_dejeuner = "Choix invalide"

    # Dîner
    if diner == 1:
        nom_diner = "Sandwich"
    elif diner == 2:
        nom_diner = "Dürüm"
    elif diner == 3:
        nom_diner = "Pastabox"
    else:
        nom_diner = "Choix invalide"

    # Souper
    if souper == 1:
        nom_souper = "Pâtes bolognaise"
    elif souper == 2:
        nom_souper = "Steak frites"
    elif souper == 3:
        nom_souper = "Saumon fumé"
    else:
        nom_souper = "Choix invalide"

    # Affichage des choix
    print(f"\n--- Vos choix pour {jour[i]}---")
    print(f"Déjeuner : {nom_dejeuner}\n")
    print(f"Dîner : {nom_diner}\n")
    print(f"Souper : {nom_souper}\n\n\n")
    i = i +1
    commande = input("Voulez-vous choisir vos plats pour un autre jour?\n 1. Oui 2. Non\n") == "1"
    if i >= 7:
        print("Les menus ne sont disponible qu'une semaine à la fois")
        break