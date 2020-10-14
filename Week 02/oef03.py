from datetime import datetime
geboortejaar = int(input("geef uw geboortejaar:>"))
geboortemaand = int(input("Geef uw geboortemaand als getal: >"))

huidig_jaar = datetime.now().year
huidige_maand = datetime.now().month

print(f"{huidige_maand}")

leeftijd = huidig_jaar - geboortejaar

if leeftijd > 17:
    # u bent sowieso volwassen
    print("u bent volwassen, u mag alco drinken")
elif leeftijd > 17:
    # u bent op jaartal nog 17, maar wel verjaard, u bent dus volwassen.
    if geboortemaand < huidige_maand:
        print("u bent al jarig geweest, u mag alco drinken")
    else:
        # u bent nog niet verjaard
        print("u bent now te jong, kom later terug")
else:
    # jonger dan 17
    print("u bent now te jong, kom later terug")