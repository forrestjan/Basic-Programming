#score = float(input("Geef uw score op: "))

# if score >= 9.5:
#print("u bent geslaagt!!")

# else:
#print("Volgende keer beter :(")
# easy versie maar werkt ook met cijfers boven 20

from math import ceil, floor

score = float(input("geef je score op 20: "))
# waarde_na_de_komma WORDT 18.5 - 18 dus 0.5(want float word omgezet nar int en rond dus af naar beneden)
waarde_na_de_komma = score - int(score)

if waarde_na_de_komma < 0.5:
    afgerond = floor(score)

else:
    afgerond = ceil(score)

print(f"je nieuwe punt is {afgerond}")

if afgerond >= 10:
    print("U bent geslaagd")

else:
    print("U bent niet geslaagd")
