current = 140.00
previous = 200.00

percent = 100*current/previous
price = 100 - percent
print(percent)
print(price)

if price > 10:
    print("Buy the product!")
    print(f"Product price reduced by {price}")
else:
    print("Dont buy the product")