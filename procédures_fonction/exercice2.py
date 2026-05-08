# Implémentez une fonction appelée recherche_min() qui prend une liste de nombres en entrée et retourne le plus petit de
# ces nombres.

def recherche_min(nbre1, nbre2, nbre3):
    """_summary_

    Args:
        nbre1 (_type_): _description_
        nbre2 (_type_): _description_
        nbre3 (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = min(nbre1, nbre2, nbre3)

    return result

resultat = recherche_min(1, 2, 3)
print(resultat)