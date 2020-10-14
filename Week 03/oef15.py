#Vraag aan de gebruiker zijn/haar howest-e-mailadres op. Haal hieruit de naam & voornaam en print
#deze af. Voor de eenvoud gaan we ervan uit dat de voornaam uit één deel bestaat. Zorg ervoor dat de
#eerste letter van de naam & voornaam met een hoofdletter afgeprint wordt.
emailadres = "tim.de.bie@student.howest.be"

atje = emailadres.find("@")
#print(f"{atje}")
voornaam_naam = emailadres[0:atje]
puntje = voornaam_naam.find(".")
voornaam = voornaam_naam[0:puntje]
naam = voornaam_naam.replace(".", " ")[puntje +1:atje]

print(f"{voornaam} {naam}")