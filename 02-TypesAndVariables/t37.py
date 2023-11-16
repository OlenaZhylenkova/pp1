john = "Mr. John May, born on 1998-02-16"

name = john[4:8]
print(f"name: {name}")
surname = john[9:12]
print(f"surname: {surname}")

initial = john[4]
initial1 = john[9]
print(f"initials: {initial, initial1}")

born = john[-10:]
print(f"born: {born}")