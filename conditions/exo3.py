import random
nombre_a_deviner = random.randint(1,10)
guess = int(input("Devinez le chiffre (1-10):\n"))

match guess:
    case _ if guess == nombre_a_deviner:
        print("Vous avez trouvé!")
    case _ if guess > nombre_a_deviner:
        print("Le nombre à deviner est plus petit")
    case _ if guess < nombre_a_deviner:
        print("Le nombre à deviner est plus grand")
    case _ if guess > 10 or guess < 1:
        print("Valeur incompatible")

print("2 essais restants")
guess = int(input("Devinez le chiffre (1-10):\n"))

match guess:
    case _ if guess == nombre_a_deviner:
        print("Vous avez trouvé!")
    case _ if guess > nombre_a_deviner:
        print("Le nombre à deviner est plus petit")
    case _ if guess < nombre_a_deviner:
        print("Le nombre à deviner est plus grand")
    case _ if guess > 10 or guess < 1:
        print("Valeur incompatible")

print("1 essai restant")
guess = int(input("Devinez le chiffre (1-10):\n"))

match guess:
    case _ if guess == nombre_a_deviner:
        print("Vous avez trouvé!")
    case _ if guess > nombre_a_deviner:
        print("Le nombre à deviner est plus petit")
    case _ if guess < nombre_a_deviner:
        print("Le nombre à deviner est plus grand")
    case _ if guess > 10 or guess < 1:
        print("Valeur incompatible")
