def check_number(x, y):
    number = int(input("A number: "))
    if number>=x and number<=y:
        print(f"Number {number} is in range [{x},{y}]: yes")
    else:
        print(f"Number {number} is in range [{x},{y}]: no")