dagen = int(input("Geef het aantal dagen op : "))
uren = int(input("Geef het aantal uren op : "))
minuten = int(input("Geef het aantal minuten op : "))
seconden = int(input("Geef het aantal seconden op : "))

#Aantal = dagen * 86400 + uren * 3600 + minuten * 60 + seconden
totaal = seconden + minuten * 60 + uren *60 * 60 + dagen *24 *60 *60
print(f"Het totale aantal seconden bedraagt:{totaal}")