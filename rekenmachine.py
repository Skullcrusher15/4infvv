getal1 = float(input("geef een eerste getal: "))
bewerking = input("welke bewerking? (+, -, *, /):")
getal2 = float(input("geef een eerste getal: "))

if bewerking == "+":
    resultaat = getal1 + getal2
    print(str(getal1) + " + " + str(getal2) + " = " + str(resultaat))
if bewerking == "-":
    resultaat = getal1 - getal2
    print(str(getal1) + " - " + str(getal2) + " = " + str(resultaat))
if bewerking == "*":
    resultaat = getal1 * getal2
    print(str(getal1) + " * " + str(getal2) + " = " + str(resultaat))
if bewerking == "/":
    resultaat = getal1 / getal2
    print(str(getal1) + " / " + str(getal2) + " = " + str(resultaat))
if bewerking == "**":
    resultaat = getal1 ** getal2
    print(str(getal1) + " ** " + str(getal2) + " = " + str(resultaat))