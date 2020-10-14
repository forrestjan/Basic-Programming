# Print alle getallen tussen 200 en 308 (grenzen inclusief) die deelbaar door 7 maar geen veelvoud van 5
# zijn.
start = 200
stop = 308
for index in range(start, stop + 1):
    if index % 7 == 0 and index % 5 != 0:
        print(f"{index}")
