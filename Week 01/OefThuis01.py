prijs_grond = float(input("wat is de prijs van uw grond?: "))
prijs_gebouw = float(input("wat is de prijs van uw gebouw?: "))
totale_prijs = prijs_grond + prijs_gebouw
totale_kost_prijs = totale_prijs + (totale_prijs / 100 * 21)

print(f"de totale kostprijs van het project is: {totale_kost_prijs:.2f}")
