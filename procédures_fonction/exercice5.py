# Écrivez une fonction convertir_temperature() qui prend une température en degrés Celsius et la convertit en degrés
# Fahrenheit

def convertir_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp = float(input("Entrez une température en dégrés celsius : \n "))
result = convertir_temperature(temp)
print(result)