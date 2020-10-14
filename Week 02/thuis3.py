def tijd_naar_bericht(naam, uur):
    if uur >= 7 and uur < 12:
        return f"Goeie morgen {naam}"
    elif uur >= 12 and uur < 13:
        return f"Goeie namidag {naam}"
    elif uur >= 13 and uur < 17:
        return f"Goeie namiddag {naam}"
    elif uur >= 17 and uur < 21:
        return f"Goeie avond {naam}"
    else:
        return f"moeje nie slapen {naam}"


naam = input("Wat is uw naam > ")
uur = int(input("hoelaat is het > "))

print(f"{tijd_naar_bericht(naam, uur)}")
