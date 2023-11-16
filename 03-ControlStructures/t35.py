i=1
while i < 31 :
    if i%3==0 and i%5!=0:
        print("THREE")
    
    if i%5==0 and i%3!=0:
        print("FIVE")
    
    if i%3==0 and i%5==0:
        print("BINGO")
    
    if i%3 != 0 and i%5 !=0 :
        print(i)
    i+=1