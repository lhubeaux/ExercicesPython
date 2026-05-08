# Créez une fonction generer_email() qui prend un prénom et un nom en entrée, et retourne une adresse e-mail
# correspondante avec un domaine prédéfini.

def generer_email(nom, prenom):
    email = nom + "." +prenom + "@email.com"
    return email

courriel = generer_email("Hubeaux", "Louis")
print(courriel)