# Créez une liste de tuples représentant les commandes d'achat avec les produits et les quantités. Ensuite, créez un
# dictionnaire de prix pour chaque produit. Calculez ensuite le coût total de toutes les commandes et affichez-le.

jantes = ('jante', 4)
pneus = ('pneu', 4)
boulons = ('boulon', 20)

commandes = [jantes, pneus, boulons]

prix = {
    'jante' : 250,
    'pneu' : 100,
    'boulon' : 20
}
cout = 0
for i in range(0, len(commandes),1):
    print(f"\nPrix de la commande de {commandes[i][0]}s : {prix.get(commandes[i][0]) * commandes[i][1]}€")
    cout = cout + prix.get(commandes[i][0]) * commandes[i][1]
print(f"\n ------------------\n \n Cout total : {cout}€\n")