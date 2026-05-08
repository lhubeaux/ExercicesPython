# Écrivez une fonction compte_mots() qui prend une chaîne de caractères représentant une phrase en entrée et retourne
# le nombre de mots dans cette phrase.

def compte_mots(phrase):
    longueur = len(phrase.split())
    return longueur

phrase_calcul = input("Veuillez entrer une phrase: \n")
resultat = compte_mots(phrase_calcul)
print(f"Votre phrase compte {resultat} mots!")
