number=int(input("number: "))


for i in range(number+1):
    for j in range(i):
        print(i, end=" ")
    print(" ")
    