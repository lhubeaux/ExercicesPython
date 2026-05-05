#Créez un programme qui permet à l'utilisateur de choisir un menu pour chaque repas (petit-déjeuner, déjeuner, dîner)
#parmi des options préétablies. Après la sélection, il affiche les choix de l'utilisateur pour chaque repas et résume
#l'ensemble des repas de la journée.

# Saisie utilisateur
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
print("\n--- Vos choix ---")
print(f"Déjeuner : {nom_dejeuner}")
print(f"Dîner : {nom_diner}")
print(f"Souper : {nom_souper}")

# Résumé de la journée
print("\n--- Résumé de la journée ---")
print(f"Votre menu du jour : {nom_dejeuner}, {nom_diner}, {nom_souper}")