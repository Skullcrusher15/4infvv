from random import randrange
getal1 = (randrange(10) + 1)
getal2 = (randrange(10) + 1)
antwoord = int(input("Hoeveel is " + str(getal1) + " x " + str(getal2) + "? "))

if antwoord == getal1 * getal2:
    print("Juist, goed zo!")
else:
    print("Fout! Het juiste antwoord is", getal1 * getal2)