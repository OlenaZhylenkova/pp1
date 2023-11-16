number = int(input("enter number: "))

i=1
k=2
while i<number+1:
    print("*"*i)
    i+=1    
    if i == number+1:
        k=2
        while k>0 and k < number+1:
            print("*"*(i-k))
            k+=1



        