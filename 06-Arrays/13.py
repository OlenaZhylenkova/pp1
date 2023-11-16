# 13.	Create a program that displays the name of month for a given month number (1 to 12). Define a month(n) function that returns the name of month for the number n. Store month names in an array. Using defined function, display month names for the following month numbers: 1, 2, 11, 12.

months= ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]


def f(n):
    for i in range(len(months)):
        if n == i:
            print(months[i-1])
        else:
            continue

f(4)