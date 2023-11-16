time = input("enter time:  ")

if int(time[0:2]) < 13: 
    print(f"{time} am")
else:
    time_changed = int(time[0:2])-12
    print(f"{time_changed}:{time[3:5]} PM")