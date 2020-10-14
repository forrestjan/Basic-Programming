# Vraag aan de gebruiker zijn naam, voornaam en geboortedatum (formaat: dd-mm-yyyy) op. Genereer
# hiermee een paswoord door:
# - de eerste 3 karakters van de ingegeven familienaam (in kleine letters en zonder de eventuele
# spaties mee te nemen)
# - de eerste 2 karakters van de voornaam (in hoofdletters en ook zonder spaties)
# - 4 cijfers (mmyy) uit de geboortedatum.
# Maak hiervoor een afzonderlijke functie ‘genereer_paswoord’. Welke parameters gebruik je, wat zal de
# return waarde zijn?


def genereer_paswoord(naam, voornaam, geboortedatum):
    # eerste drie letters uit de naam halen
    sub_naam = naam.replace(" ", "")[0:3]
    # eerste twee letters uit de voornaam halen
    sub_voornaam = voornaam[0:2]
    # maand en jaar uit geboortedatum halen
    sub_geboortedatum = geboortedatum[3:5] + geboortedatum[8:10]

    return f"{sub_naam.lower()}{sub_voornaam.upper()}{sub_geboortedatum}"


paswoord = genereer_paswoord("Walcarius", "Stijn", "30-08-2019")
print(f"het paswoord is: {paswoord}")
