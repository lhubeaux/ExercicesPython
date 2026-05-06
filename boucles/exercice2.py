# Créez un programme qui demande à l'utilisateur d'entrer son âge. Utilisez un opérateur ternaire pour vérifier si
# l'utilisateur est majeur ou mineur. Affichez ensuite un message approprié en fonction de la réponse.

age = int(input("Quel âge avez vous? \n"))
user_majeur = 'majeur'

user_majeur = "majeur" if age >= 18 else "mineur"

print(f"L'utilisateur est {user_majeur}")