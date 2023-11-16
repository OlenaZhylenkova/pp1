import random

randomnum = random.randint(1,6)
if randomnum == 6 or randomnum == 1:
    print(f"dice rolled :{randomnum}")
    print("True")
else: 
    print(f"dice rolled :{randomnum}")
    print("False")