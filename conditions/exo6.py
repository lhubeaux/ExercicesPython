# Créez un programme qui génère des citations aléatoires à partir d'un nombre aléatoire. L'utilisateur devrait pouvoir
# choisir un thème et le programme générera une citation aléatoire correspondante. Utilisez des correspondances pour
# gérer les différents thèmes et générer les citations appropriées.

theme = int(input("Quel thème pour la citation? 1. philosophique 2. rap \n"))
citation_number = int(input("Quelle citation souhaitez vous? Choisissez un nombre entre 1 et 3\n"))

match theme, citation_number:
    case 1, 1:
        print("\"Je sais que je ne sais rien.\" \n -Aristote")
    case 1, 2:
        print("\"Je pense, donc je suis.\" \n -René Descartes")
    case 1, 3:
        print("\"La vie n'est pas un problème à résoudre mais une réalité dont il faut faire l'expérience? \" \n -Søren Kierkegaard")
    case 2, 1: 
        print("\"Les femmes viennent de Vénus. Les hommes mangent des Mars.\" \n -MC Solaar")
    case 2, 2:
        print("\"Vieillir est une obligation mais grandir est un choix.\" \n -Youssoupha")
    case 2, 3:
        print("\"J'nique des mères à toute vitesse, ma queue a syndrome de la Tourette\" \n -Booba")