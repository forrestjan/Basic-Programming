# Maak een applicatie dat aan de gebruiker een aantal in te voeren producten vraagt. Vervolgens loop je
# dat aantal af en vraag je telkens bij elk product op:
# - De categorie op: de gebruiker kiest tussen “Groente”, “Fruit”, “Drank”.
# - De kostprijs van het product
# Print op het einde per categorie de totale kost op, alsook de gemiddelde prijs per categorie af.
aantal_producten = int(input("hoeveel producten wens je in te geven > "))
aantal_groenten = 0
aantal_fruit = 0
aantal_drank = 0

prijs_groenten = 0
prijs_fruit = 0
prijs_drank = 0

for index in range(0, aantal_producten):
    categorie = input("Welke categorie? (F:Fruit, G:Groente, D:drank) > ")
    prijs = float(input("wat is de prijs van het product"))
    if categorie.upper() == "F":
        aantal_fruit += 1
        prijs_fruit += prijs
    elif categorie.upper() == "G":
        aantal_groenten += 1
        prijs_groenten += prijs
    elif categorie.upper() == "D":
        aantal_drank += 1
        prijs_drank += prijs
    else:
        print("dit is een ongeldige keuze")
# In deze oefening zullen er fouten optreden indienn geen producten in de categorie aanwezig zijn
print(f"er zijn {aantal_fruit} stuks fruit.")
print(f"de totale prijs van het fruit is {prijs_fruit}")
print(f"de gemiddelde fruitprijs is {prijs_fruit / aantal_fruit}")

print(f"er zijn {aantal_groenten} stuks groenten.")
print(f"de totale prijs van het groenten is {prijs_groenten}")
print(f"de gemiddelde groentenprijs is {prijs_groenten / aantal_groenten}")

print(f"er zijn {aantal_drank} stuks drank.")
print(f"de totale prijs van het drank is {prijs_drank}")
print(f"de gemiddelde drankprijs is {prijs_drank / aantal_drank}")
