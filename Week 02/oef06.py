woord1 = input("Geef een eerst woord: ")
woord2 = input("Geef een tweede woord: ")

if woord1 == woord2:
    print("de woorden zijn gelijk")

else:
    print("de woorden zijn niet gelijk")

if str.lower(woord1) == str.lower(woord2):
    print("De woorden zijn volledig gelijk")

else:
    print("de woorden zijn niet volledig gelijk")
