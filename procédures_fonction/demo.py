# print(f"1. Procédure - Ne renvoie rien \n {"=" * 50}")


# def demoProcedure(prenom="Toto"): #Si on ne donne pas de paramètre lors de l'appel ça sera Toto qui sera indiqué
#     """_summary_

#     Args:
#         prenom (str, optional): _description_. Defaults to "Toto".
#     """
#     print("Bonjour,", prenom)
#     print("Bienvenue dans ma procédure")
#     print("=" * 30)

# demoProcedure("Louis")


print(f"2. Fonction - Retourne une valeur \n {"=" * 50}")


def demoFonction(prenom="Toto"): #Si on ne donne pas de paramètre lors de l'appel ça sera Toto qui sera indiqué
    phrase_retour = ""
    """_summary_

    Args:
        prenom (str, optional): _description_. Defaults to "Toto".

    Returns:
        _type_: _description_
    """
    phrase_retour +=f"Bonjour {prenom}\n"
    phrase_retour += "Bienvenue dans ma fonction"

    return phrase_retour
    

result = demoFonction()
print(result)