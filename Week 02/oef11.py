def toon_max(getal1, getal2, getal3):
    if getal1 > getal2 and getal1 > getal3:
        return getal1
    elif getal2 > getal3 and getal2 > getal1:
        return getal2
    else:
        return getal3


getal1 = int(input("geef nmr"))
getal2 = int(input("geef nmr"))
getal3 = int(input("geef nmr"))
print(f"het grootste getal is: {toon_max(getal1,getal2,getal3)}")
