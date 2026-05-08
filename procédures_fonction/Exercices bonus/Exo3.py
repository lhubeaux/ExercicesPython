# Implémentez une fonction analyser_frequence_lettres(texte) qui retourne un dictionnaire avec
# la fréquence en pourcentage de chaque lettre de l’alphabet (a-z), trié par fréquence
# décroissante. Ignorez les majuscules, espaces et caractères spéciaux. Retournez également la
# lettre la plus fréquente et la moins fréquente.

from collections import Counter
import string

def paire(p):   # paire = paramètre
    return p[1]       # paire = même paramètre utilisé dans le corps

def analyser_frequence_lettres(texte):
    lettres = []
    for char in texte.lower():
        if char in string.ascii_lowercase:
            lettres.append(char)
    comptage = Counter(lettres)
    total = len(lettres)
    frequences = {}
    for lettre, nombre in comptage.items():
        frequences[lettre] = round(nombre / total * 100, 2)
    
    frequences = dict(sorted(frequences.items(), key = paire, reverse = True))
    lettre_max = max(frequences, key = frequences.get)
    lettre_min = min(frequences, key = frequences.get)
    
    
    return frequences, lettre_max, lettre_min

frequences, lettre_max, lettre_min = analyser_frequence_lettres("Je m'appelle Louisaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print("----- Voici un tableau de la fréquence pour chaque lettre du texte -----")
print(f"{'Lettre':<10} | {'Fréquence':<10}")
print("-" * 25)
for lettre, freq in frequences.items():
    print(f"{lettre:<10} | {freq:<10}%")
print(f"La lettre la plus courante est {lettre_max}")
print(f"La lettre la moins courante est {lettre_min}")