hours = input("Enter hours: ")
rate = input("Enter Rate: ")
h = float(hours)
r = float(rate)
pay = h*r
rounded = round(pay, 2)
print("Pay: ", rounded)