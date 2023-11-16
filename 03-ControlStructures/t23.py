age = int(input("Enter the dog's age in human years: "))

first = 10.5
second = 4

if age <= 2:
    agedog = age*10.5
    print(f"Dog's years : {agedog}")
else:
    agedog = 2*10.5 + (age-2)*4
    print(f"Dog's years: {agedog}")