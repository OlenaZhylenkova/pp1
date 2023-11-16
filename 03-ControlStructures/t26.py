car_speed = int(input("Enter car speed: "))
speed_limit_max = 140
speed_limit_min = 40

if car_speed > speed_limit_max or car_speed < speed_limit_min:
    print("Invalid car speed")
else:
    print("valid car speed")