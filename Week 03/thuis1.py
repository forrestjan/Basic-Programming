string = input("Geef een woord: >")
count_lower = 0
for i in string:
    if(i.islower()):
        count_lower = count_lower+1
print(f"aantal lowercase letters zijn {count_lower}")

count_high = 0
for i in string:
    if(i.isupper()):
        count_high = count_high + 1
print(f"aantal uppercase letters zijn {count_high}")
