price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

pwd = price * discount /100
reduction = price - pwd
print(f"Price with discount: {round(reduction, 2)}")
print(f"Reduction: {round(pwd, 2)}")