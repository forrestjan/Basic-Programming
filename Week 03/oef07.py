# Vraag aan de gebruiker volgende 3 getallen op:
# - een startwaarde
# - een positieve stapgrootte
# - het gewenste aantal af te printen getallen
# Schrijf een functie ‘print_lijst_getallen’ die deze 3 getallen als parameter binnen krijgt. De functie print
# een lijst, met het gewenste aantal getallen, af waarbij het eerste getal gelijk is aan de startwaarde en de
# getallen met de stapgrootte vergroten.De functie heeft geen return waarde. Het afprinten gebeurt IN de
# functie.


def print_lijst_getallen(start, stap, aantal):
    stop = start + (stap * aantal)
    # print(f"{stop}")
    for getal in range(start, stop, stap):
        print(f"{getal}")


startwaarde = int(input("Wat is de startwaarde?"))
stapgrootte = int(input("Wat is de stapgrootte?"))
aantal_getallen = int(input("hoeveel getallen wil u zien?"))
print_lijst_getallen(startwaarde, stapgrootte, aantal_getallen)
