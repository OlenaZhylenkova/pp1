ean = input("Enter EAN-13 article number: ")

if len(ean) == 13 and ean[0:3] == "590":
    print("Manufactured in Poland")
elif len(ean) == 13 and ean[0:3] != "590":
    print("Not manufactured in Poland")
else:
    print("Invalid EAN-13")