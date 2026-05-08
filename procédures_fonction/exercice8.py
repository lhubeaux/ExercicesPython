# Créez une fonction valider_mot_de_passe() qui prend un mot de passe en entrée et vérifie s'il répond à certains
# critères de complexité (longueur minimale, présence de chiffres, de lettres majuscules et minuscules, de caractères
# spéciaux, etc.). La fonction devrait renvoyer True si le mot de passe est valide et False sinon.

def valider_mot_de_passe(mdp):
    # Vérification de la longueur
    if len(mdp) < 8:
        return False
    
    # Vérification de la présence d'une majuscule
    majuscule = False
    for i in mdp:
        if i.isupper():
            majuscule = True
    if majuscule == False:
        return False
    
    # Présence de minuscules
    minuscule = False
    for j in mdp:
        if j.islower():
            minuscule = True
    if minuscule == False:
        return False
    
    # Présence de chiffres
    chiffre = False
    for k in mdp:
        if k.isdigit():
            chiffre = True
    if chiffre == False:
        return False
    
    # Présence de caractères spéciaux
    speciaux = False
    specials = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    for s in mdp:
        if s in specials:
           speciaux = True
    if speciaux == False:
        return False
    else:
        return True
    
motdep = input("Veuillez entrer votre mot de passe : \n")
if valider_mot_de_passe(motdep) == True:
    print("Mot de passe correct!")
else: print("Veuillez corrigr votre mot de passe")