start = 99
stop = 0

tekst = ""

# indien de startwaarde even is maak er oneven van


for index in range(start, stop - 1, -3):
    if start % 2 != 0:
        tekst = tekst + "-" + str(index)
    # alternatief
    # tekst = f"{tekst} - {index}

print(f"{tekst}")
