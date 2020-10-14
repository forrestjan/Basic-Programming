broek = float(70.5)
tshirt = float(20.89)
vest = float(100.3)

aantal_broeken = int(input("Hoeveel broeken werden er gekocht? "))
aantal_tshirts = int(input("Hoeveel tshirts werden er gekocht? "))
aantal_vesten = int(input("Hoeveel vesten werden er gekocht? "))
totaal_bedrag = (broek * aantal_broeken) + (tshirt * aantal_tshirts) + (vest * aantal_vesten)

print("***welkom bij het kassa systeem***")
print(f"Hoeveel broeken werden er gekocht? {aantal_broeken}")
print(f"Hoeveel T-shirts werden er gekocht? {aantal_tshirts}")
print(f"Hoeveel vesten werden er gekocht? {aantal_vesten}") 
print(f"Totaal te betalen:\n{totaal_bedrag}")  