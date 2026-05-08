# Créez une fonction encoder_message(texte, decalage) qui chiffre un texte avec le chiffrement
# de César. La fonction doit gérer les minuscules, majuscules, les accents (é, è, à, etc.), et laisser
# les caractères non alphabétiques inchangés. Elle doit également proposer un mode
# déchiffrement si le décalage est négatif.

def encoder_message(texte, decalage):
    accents = {
    'é': 'e', 'à': 'a', 'â': 'a', 'ä': 'a', 'ç': 'c',
    'è': 'e', 'ê': 'e', 'ë': 'e',
    'î': 'i', 'ï': 'i',
    'ô': 'o', 'ö': 'o',
    'ù': 'u', 'û': 'u', 'ü': 'u', 'ÿ': 'y',
    'À': 'A', 'Â': 'A', 'Ä': 'A', 'Ç': 'C',
    'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
    'Î': 'I', 'Ï': 'I',
    'Ô': 'O', 'Ö': 'O',
    'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ÿ': 'Y'
}
    alphabet_min = "abcdefghijklmnopqrstuvwxyz"
    alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for char in texte:
        if char in accents:
            char = accents[char]
            if char in alphabet_maj:
                pos = alphabet_maj.index(char)
                nouvelle_pos = (pos + decalage) % 26
                char = alphabet_maj[nouvelle_pos]
            elif char in alphabet_min:
                pos = alphabet_min.index(char)
                nouvelle_pos = (pos + decalage) % 26
                char = alphabet_min[nouvelle_pos]

        elif char in alphabet_min:
            pos = alphabet_min.index(char)
            nouvelle_pos = (pos + decalage) % 26 
            char = alphabet_min[nouvelle_pos]

        elif char.isupper():
            pos = alphabet_maj.index(char)
            nouvelle_pos = (pos + decalage) % 26
            char = alphabet_maj[nouvelle_pos]
        
        else:
            pass
        
        result.append(char)
    return "".join(result)
print(encoder_message("Louis", 2))
print(encoder_message("Nqwku", -2))