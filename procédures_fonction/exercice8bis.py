# Créez une fonction valider_mot_de_passe() qui prend un mot de passe en entrée et vérifie s'il répond à certains
# critères de complexité (longueur minimale, présence de chiffres, de lettres majuscules et minuscules, de caractères
# spéciaux, etc.). La fonction devrait renvoyer True si le mot de passe est valide et False sinon.

def valider_mot_de_passe(mdp):
    # Vérifications
    specials = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    if len(mdp) > 8 and any(i.isupper() for i in mdp) and any(i.islower() for i in mdp) and any(i.isdigit() for i in mdp) and any(i in specials for i in mdp):
        return True
    else:
        return False

    
    
motdep = input("Veuillez entrer votre mot de passe : \n")
if valider_mot_de_passe(motdep) == True:
    print("Mot de passe correct!")
else: print("Veuillez corrigr votre mot de passe")