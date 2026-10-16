aantal1 = input("Hoeveel taakjes heb je uitgevoerd?")
aantal1 = int(aantal1)
aantal2 = input("Hoeveel keer heb je de tafel niet afgeruimd?")
aantal2 = int(aantal2)
aantalzakgeldperweek = 5 
perweek = int(aantalzakgeldperweek + (aantal1 * 2 ) - (aantal2))
print(f"Lio krijgt {perweek} euro per week")