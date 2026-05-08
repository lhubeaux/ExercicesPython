# Implémentez une fonction inverser_chaine() qui prend une chaîne de caractères en entrée et retourne cette chaîne
# inversée.
def inverser_chaine(phrase):
    inverse = ""
    for i in range(len(phrase) -1, -1, -1):
        inverse = inverse + phrase[i]

    return inverse

entree = input("Veuillez entrer une phrase à inverser: \n")
result = inverser_chaine(entree)
print(result)