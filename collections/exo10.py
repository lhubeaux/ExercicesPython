# Créez une liste de dictionnaires représentant les informations des employés avec leur nom, salaire et département.
# Calculez la somme des salaires pour chaque département, puis calculez la moyenne des salaires pour chaque
# département. Enfin, affichez les moyennes des salaires pour chaque département.

employes = [
    {"nom": "Alice",   "salaire": 3500, "departement": "RH"},
    {"nom": "Bob",     "salaire": 4200, "departement": "IT"},
    {"nom": "Claire",  "salaire": 3800, "departement": "RH"},
    {"nom": "David",   "salaire": 5100, "departement": "IT"},
    {"nom": "Eva",     "salaire": 4600, "departement": "Finance"},
    {"nom": "Frank",   "salaire": 3200, "departement": "Finance"},
    {"nom": "Grace",   "salaire": 4900, "departement": "IT"},
]

# Salaire par département
total_salaires = {}
total_employes = {}
for i in range(0, len(employes),1):
    departement = employes[i]['departement']
    salaire = employes[i]["salaire"]
    
    if departement in total_salaires:
        total_salaires[departement] += salaire
        total_employes[departement] += 1
    
    else:
        total_salaires[departement] = salaire
        total_employes[departement] = 1
        
for departement in total_salaires:
    print(f"\nLe département {departement} compte {total_employes.get(departement)} employés pour un salaire total de {total_salaires.get(departement)}€")
    print(f"Le salaire moyen pour le département {departement} est de {total_salaires.get(departement) / total_employes.get(departement)}€\n----")