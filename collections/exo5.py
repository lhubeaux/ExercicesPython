# Créez une liste de tuples contenant le nom et l'âge de trois personnes. Trouvez ensuite la personne la plus âgée et
# affichez son nom.

personne1 = ('jean', 20)
personne2 = ('michel', 25)
personne3 = ('pauline', 30)

people = [personne1, personne2, personne3]
age = 0
nom = 'a'
for i in range(1, len(people),1):
    if people[i][1] > age:
        nom = people[i][0]
        age = people[i][1]
print(f"Le plus vieux ou la plus vieille est {nom}, cette personne a {age} ans")