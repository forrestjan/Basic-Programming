aantal_seconden = int(input("geef het aantal seconden op"))

#aantal dagen uit de seconden halen
dagen = aantal_seconden // (24 * 60 * 60)

#overgebleven seconden berekenen
aantal_seconden = aantal_seconden % (24 * 60 * 60)

#aantal uren uit de overgebleven seconden halen
uren = aantal_seconden // (60 * 60)

#overgebleven seconden berekenen
aantal_seconden = aantal_seconden % (60 * 60)

#aantal minuten uit de overgebleven seconden halen
minuten = aantal_seconden // 60

#overgebleven seconden berekenen
seconden = aantal_seconden % 60

print(f"d:h:m:s ---> {dagen}:{uren}:{minuten}:{seconden}")



# // is gehele deeling bijvoorbeeld 124//2 = 2 maar 124/2 is 2.06 
# gehele deling geeft je rest niet weer


