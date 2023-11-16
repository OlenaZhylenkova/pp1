# 51.	Define a function sum(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n. Apply recursion. Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum(n):
    sum =0
    for i in range(0,n+1):
        sum = sum + i
    return sum

print(sum(10))

def sum_ten():
    sum = 0 
    for i in range(0,11):
        sum = sum + i
    return sum

print(sum_ten())