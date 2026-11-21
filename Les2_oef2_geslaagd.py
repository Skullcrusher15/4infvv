punten = (float(input("hoeveel punten heb je behaald?")))
totaal = (float(input("Op hoeveel punten was de toets?")))
percentage = punten / totaal * 100
print("Je hebt " + str(round(percentage,1)))

if percentage >= 50:
    print("procifiat,je bent geslaagd")
if percentage < 50:
    print("jammer,je bent niet geslaagd")