# Créez un dictionnaire de listes représentant différents cours et les étudiants inscrits dans chaque cours. Ajoutez des
# étudiants à chaque cours. Ensuite, demandez à l'utilisateur de saisir le nom d'un cours et affichez la liste des
# étudiants inscrits à ce cours.

cours = {
    'maths' : ['William', 'Pauline', 'Emmanuel'],
    'français' : ['Louis', 'Andreas', 'Greg', 'Jimmy'],
    'histoire' : ['Adrien', 'Charlotte', 'Emilie']
}

choix = input("Veuillez choisir le cours pour lequel vous voulez voir les participants: \n maths, histoire ou français\n Votre choix : ")
print(f"Voici les élevèes pour le cours de {choix} {cours.get(choix)}")