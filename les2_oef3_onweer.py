aantalseconden = int(input("hoeveel seconden zitten er tussen de bliksem en de donder?"))
aantalkilometer = (aantalseconden * 343) / 1000
print("Het onweer is " + str(round(aantalkilometer)) + " kilometer ver weg")

if aantalkilometer < 3:
    print("Opgelet! Het onweer is dichtbij. Ga snel naar binnen!")

