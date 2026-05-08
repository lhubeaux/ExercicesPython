def valider_mot_de_passe(mdp):
    specials = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    maj = False
    min_ = False
    chiffre = False
    special = False
    for i in mdp:
        if i.isupper(): maj = True
        if i.islower(): min_ = True
        if i.isdigit(): chiffre = True
        if i in specials: special = True
    if len(mdp) >= 8 and maj and min_ and chiffre and special == True:
        return True
    return False

motdep = input("Veuillez entrer votre mot de passe : \n")
if valider_mot_de_passe(motdep) == True:
    print("Mot de passe correct!")
else: print("Veuillez corriger votre mot de passe")