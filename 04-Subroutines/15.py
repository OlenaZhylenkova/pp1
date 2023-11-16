# 15.
# def keyboard():
#     for i in range(1,10):
#         print(i, end=" ")
#         if i %3 == 0:
#             print()
#     print()

# keyboard()

# 16.	Define a function product(x, y) that displays a product of two numbers. Then, call the function.
# def product(x,y):
#     return x*y

# a = 3
# b = 4
# print(f"The product of {a} and {b} is {product(a,b)}")


# def product(x,y):
#     return x*y


# a= 3
# b=4
# print(product(a,b))


# 17.	Define the function different(n1,n2,n3), which returns True if all three numbers n1,n2,n3 are different or False otherwise. Then, write a program that reads three integers from the keyboard. Checks whether the numbers are different. Sample result:
# Enter first number: …
# Enter second number: …
# Enter third number: …
# Numbers …, …, and … are different


# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# n3=int(input("Enter third number: "))
# def different(n1,n2,n3):
#     if n1==n2 and n1==n3:
#         print("True")
#     else:
#         print("False")
# different(n1,n2,n3)

# 18.	Define a function numbers(n) that returns a string containing integer numbers from 1 to n, separated by a single space character. Then, call the function and display numbers from 1 to 15 and from 1 to 7. Sample result:
# Numbers <1,15>: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# Numbers <1,7>: 1 2 3 4 5 6 7
# Modules

# n = int(input("Enter your number: "))
# def numbers(n):
#     for i in range(1, n+1):
#         print(i, end=" ")
# numbers(n)


# 19.	In a separate module, define a function that calculates the sum of digits. Use the function to calculate the sum of digits entered from the keyboard. To do it, copy the following modules. Then, run the programs digits.py and myprogram.py separately. Try to analyze the results. Do you understand how to import a module and how to call the functions contained in the module?
# digits.py
# def sum_digits(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     return sum

# if __name__ == "__main__":
#     # check if function works
#     print(sum_digits(7182))
#     print(sum_digits(0))
#     print(sum_digits(333))
# myprogram.py
# import digits

# number = int(input("Enter a number: "))
# sum_d = digits.sum_digits(number)
# msg = f"Sum of digits {number} is {sum_d}"
# print(msg)
# 20.	In the module mykeyboard.py, define a function read_number() that returns an integer number entered from the keyboard. The function should print a text prompting user to enter data 'Enter a number: '. Then, use the function to read two numbers from the keyboard. To test the function, use the __name__ variable. Display the sum of two entered numbers. Sample result:
# Enter a number: 34
# Enter a number: 7
# 34 + 7 = 41
