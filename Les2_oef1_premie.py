uren = float(input("Hoeveel uur heb je deze maand gewerkt?: "))
uurloon = 8.5

if uren > 20:
    Loon = uren * uurloon + 25

    print("proficiat, Je krijgt een premie van 25 euro!")
    print("Je loon is " + str(round(Loon,2)))

if uren <= 20:
    Loon = uren * uurloon
    print("Je hebt " + str(round(Loon,2)) + " euro verdient")