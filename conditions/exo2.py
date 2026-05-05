note = int(input("Introduisez votre note entre 0 et 20 :\n"))

match note:
    case _ if 15 <= note <= 20:
        print("Très bien ✔")
    case _ if 10 <= note <= 14:
        print("Satisfaisant ⚠")
    case _ if 0 <= note <= 9:
        print("Insuffisant ‼")
    case _ if note > 20 and note < 0 :
        print("Veuillez entrer une valeur correcte")