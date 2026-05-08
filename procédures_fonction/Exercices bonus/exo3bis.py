# Code réalisé par Claude pour pouvoir comparer avec la version utilisant les bibliothèques, le tout basé sur ma première version

def paire(p):
    return p[1]

def analyser_frequence_lettres(texte):
    comptage = {}
    for char in texte:
        if char.isalpha():
            if char not in comptage:
                comptage[char] = 1
            else:
                comptage[char] += 1

    total = sum(comptage.values())

    frequences = {}
    for lettre, nombre in comptage.items():
        frequences[lettre] = round(nombre / total * 100, 2)

    frequences = dict(sorted(frequences.items(), key=paire, reverse=True))

    lettre_max = max(frequences, key=frequences.get)
    lettre_min = min(frequences, key=frequences.get)

    return frequences, lettre_max, lettre_min

frequences, lettre_max, lettre_min = analyser_frequence_lettres("")

print("----- Voici un tableau de la fréquence pour chaque lettre du texte -----")
print(f"{'Lettre':<10} | {'Fréquence':<10}")
print("-" * 25)
for lettre, freq in frequences.items():
    print(f"{lettre:<10} | {freq:<10}%")

print(f"\nLa lettre la plus courante est : {lettre_max}")
print(f"La lettre la moins courante est : {lettre_min}")