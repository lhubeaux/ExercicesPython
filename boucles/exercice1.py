#Concevez un programme qui génère et affiche les nombres premiers jusqu'à 100 en utilisant une boucle.

for n in range(2, 101):
    if all(n % d != 0 for d in range(2, n)):
        print(f"{n} est un nombre premier")