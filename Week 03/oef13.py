#Schrijf een functie ‘swap’ die twee strings binnenkrijgt. De functie stelt één nieuwe string op waarbij de
#twee letters van elk woord worden omgewisseld en beide nieuwe woorden door een spatie gescheiden
#worden.
#Het resultaat van de functie is de nieuwe string.
#Voorbeeld: “abc” en “xyz” à “xyc abz”
def swap (string1, string2):
    sub_string1 = string1 [:2] + string2[2:]
    sub_string2 = string2[:2] + string1[2:]
    return f"{sub_string2} {sub_string1}"

swapping = swap("abc", "xyz")
print(f"{swapping}")