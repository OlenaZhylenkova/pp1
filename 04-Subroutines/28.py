# 28.	The binary numerical system uses two symbols to represent a number: 0 and 1. Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, or False otherwise. Sample result:
# f("101101") returns True
# f("1311a10100") returns False

def f(binary_number):
    count = 0
    for i in binary_number:
        if i == "0" or i == "1":
            count+=1
            continue
        else:
            print("Not a binary number")
            break
    
    if count == len(binary_number):
        print(f"{binary_number} is a Binary number")
        
    

f("01010g0")