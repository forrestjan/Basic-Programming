leeftijd_hond = int(input("Geef de leeftijd van uw hond"))

if leeftijd_hond < 0:
    print("ongeldige input")

elif leeftijd_hond == 0:
    print("het is een puppy")

elif leeftijd_hond == 1:
    print("komt overeen met 14 mensenjaren")

elif leeftijd_hond == 2:
    print("komt overeen met 22 mensenjaren")

else:
    berekende_leeftijd = 22 + (leeftijd_hond - 2) * 5
    print(f"komt overeen met {berekende_leeftijd} mensenjaren")
