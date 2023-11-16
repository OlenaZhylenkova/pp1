# 29.	The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:
# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

def f(amount_to_pay):
    coins = 0
    if amount_to_pay > 5:
        fives = amount_to_pay // 5
        leftover = amount_to_pay%5
    if leftover > 2:
        twos = leftover // 2
        leftover_two = leftover%2
    if leftover_two == 1:
        one = 1
    coins = fives + twos + 1
    return print(coins)
f(8)