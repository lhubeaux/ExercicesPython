# Écrivez une fonction moyenne_ponderee(notes, coefficients) qui prend deux listes de même
# longueur et calcule la moyenne pondérée. La fonction doit gérer les cas où les listes n’ont pas la
# même taille, où une liste est vide, et retourner un message d’erreur clair dans ces cas (sous
# forme de tuple : (moyenne, message)).

liste_moyenne = [2, 18, 29, 6, 19]
liste_coefficents = [1, 3, 2, 1/3, 1]

def moyenne_ponderee(notes, coeffcients):
    if len(notes) == 0 or len(coeffcients) == 0:
        message = 'Une des deux listes est vide'
        moyenne = 0
    elif len(notes) != len(coeffcients):
        message = 'Les listes sont de taille différente'
        moyenne = 0
    else:
        liste_result = []
        for i in range(0, len(notes),1):
            liste_result.append(notes[i]*coeffcients[i])
        moyenne = sum(liste_result) / sum(coeffcients)
        message = f'La moyenne pondérée vaut {moyenne}'
    return (moyenne, message)

result = moyenne_ponderee(liste_moyenne, liste_coefficents)
print(result)