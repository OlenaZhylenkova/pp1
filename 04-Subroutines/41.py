# 41.	Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:
# f(1) returns 2
# f(5) returns 11

def is_prime(n):
    if n <=1:
        return False
    elif n <=3:
        return True
    elif n%2==0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2) == 0:
            return True
        i +=6
    return True

def nth_prime(n):
    if n == 1:
        return 2
    count = 1
    num = 3
    while count < n:
        if is_prime(num):
            count +=1
        if count < n:
            num +=2
    print(num)
    return num

nth_prime(5)

