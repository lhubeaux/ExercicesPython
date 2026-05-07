# Générez deux ensembles de nombres aléatoires compris entre 1 et 20. Affichez ces deux ensembles générés. Enfin,
# trouvez l'intersection des deux ensembles et affichez-la

import random
ensemble1=set()
for i in range (1,10,1):
    ensemble1.add(random.randint(1,20))
print(ensemble1)

import random
ensemble2=set()
for i in range (1,10,1):
    ensemble2.add(random.randint(1,20))
print(ensemble2)

intersection = ensemble1.intersection(ensemble2)

print(f"Nombres communs aux deux ensembles = {intersection}")