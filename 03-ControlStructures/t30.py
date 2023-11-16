x = int(input("X: "))
y = int(input("Y: "))

if x>0 and y>0:
    print(f"Point P({x},{y}) is in the 1st q.")
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the 4th q.")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the 2nd q.")
else:
    print(f"Point P({x},{y}) is in the 3rd q")