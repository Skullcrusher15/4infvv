from random import randrange
geheim = (randrange(10) + 1)
gok = int(input("raad een getal van 1 tot en met 10: "))

if gok == geheim:
    print("Gewonnen! Het getal was " + str(geheim))

if gok != geheim:
    print("Jammer! Het juiste getal was " + str(geheim))
