decimal = int(input("Enter a decimal number: "))

bin = []
while decimal:
    bin.append(decimal%2)
    decimal >>=1
print(bin[::-1])
