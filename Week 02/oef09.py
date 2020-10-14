<< << << < HEAD


def maak_verwelkoming_klas(naam, klasgroep="1MIT1"):
    return f" welkom {naam} in {klasgroep}"


naam = input("geef uw naam op: ")
groep = input("wat uw groep?: ")

resultaat = maak_verwelkoming_klas(naam, groep)
print(resultaat)

tweede_resultaat = maak_verwelkoming_klas(naam)
print(tweede_resultaat)

== == == =


def maak_verwelkoming_klas(naam, klasgroep):
    klasgroep = "1MIT1"
    return f" welkom {naam} in {klasgroep}"


naam = input("geef uw naam op")

print(maak_verwelkoming_klas)
