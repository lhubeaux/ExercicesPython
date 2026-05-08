# Écrivez une fonction nommée calcul_moyenne() qui prend une liste de notes en entrée et retourne la moyenne de ces
# notes.

def calcul_moyenne(note1, note2, note3, note4, note5):
    """_summary_

    Args:
        note1 (_type_): _description_
        note2 (_type_): _description_
        note3 (_type_): _description_
        note4 (_type_): _description_
        note5 (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    result = (note1 + note2 + note3 + note4 +note5)/5

    return result
resultat = calcul_moyenne(5, 5, 8, 9, 4)
print(resultat)
