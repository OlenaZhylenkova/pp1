# 34.	Define the function f(n), which returns numbers from 1 to n as a string. Sample result:
# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(str(i))
    string_number = "".join(numbers)
    print(string_number)

f(11)