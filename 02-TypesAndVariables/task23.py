import math
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
p = (a+b+c)/2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Circumference: {a+b+c}, area: {s} ")