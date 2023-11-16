# 42.	Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers. Sample result:
# f(7,4,9) returns 5
# f(2,12,8) returns 10

def f(number1, number2, number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    diff = largest-smallest
    return diff

print(f(7,4,9))

