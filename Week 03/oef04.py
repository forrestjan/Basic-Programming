start = 10
stop = 129

tekst = ""

# indien de startwaarde even is maak er oneven van
if start % 2 == 0:
    start = start + 1

for index in range(start, stop + 1, 2):
    tekst = tekst + "-" + str(index)
    # alternatief
    # tekst = f"{tekst} - {index}
print(f"{tekst}")
