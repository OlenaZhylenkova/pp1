import random
randomdice = random.randint(1,6)
yourdice = int(input("Make a guess: "))

if randomdice == yourdice:
    print(f"computers'dice: {randomdice}")
    print(f"your guess: {yourdice}")
    print("True")
else:
    print(f"computers'dice: {randomdice}")
    print(f"your guess: {yourdice}")
    print("False")