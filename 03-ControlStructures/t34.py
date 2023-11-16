money = int(input("Enter the amount in PLN: "))

if money>=5:
    five = money//5
    five_rest = money%5
    print(f"5zl: {five}")
    
if five_rest>=2:
    two = five_rest//2
    two_rest = two%2
    print(f"2zl: {two}")

if two_rest >= 1:
    one = two_rest//1
    print(f"1zL: {one}")