height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight: "))

bmi = weight/(height**2)

print (f"Your bmi:{round(bmi, 2)}")
if bmi < 18.5:
    print("underweight")
if bmi > 25:
    print("overweight")
else:
    print("normal")