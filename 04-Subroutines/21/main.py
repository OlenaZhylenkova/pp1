import mymath
import mykeyboard

random_num = mymath.number()
your_num = mykeyboard.yournumber()

def game(your_num, random_num):
    if random_num == your_num:
        print(f"Computer's number: {random_num}")
        print("True")
    else:
        print(f"Computer's number: {random_num}")
        print("False")

game(your_num, random_num)