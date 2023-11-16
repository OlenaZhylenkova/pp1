number = int(input("Number of products purchased: "))
price = int(input("Product price: "))

if number//2 == 0:
    reduced_price =price - (price*25/100)
    pay = number*reduced_price
    print(f"Total pay: {pay}")
else: 
    reduced_price =price - (price*25/100)
    pay= price + reduced_price*(number-1)
    print(f"Total pay: {pay}")