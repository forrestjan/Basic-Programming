# Laat je applicatie een getal kiezen tussen 1 en 20. Laat vervolgens de gebruiker naar het getal raden. Bij
# iedere poging krijgt hij feedback: “kleiner” of “groter”. De applicatie stopt pas als het getal geraden is.
# Je toont hoeveel maal de gebruiker gokte.
# Tip: maak uit de module ‘random’ gebruik van de functionaliteit ‘random’:
import random
# bereken van een random getal
aantal_gokjes = 1
te_raden_getal = random.randint(1, 20)


geraden_getal = int(input("Raad het getal: > "))
while te_raden_getal != geraden_getal:
    aantal_gokjes += 1
    if geraden_getal < te_raden_getal:
        print("het te geraden getal is groter")
    elif geraden_getal > te_raden_getal:
        print("het te geraden getal is kleiner")
    geraden_getal = int(input("Raad het getal: > "))
print(f"proficiat, het getal was juiste{te_raden_getal}\n je raadde {aantal_gokjes} keer")
