# 35.	Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. The available operators are +,-,*,%,**. Sample result:
# f(2,3, "+") returns 5
# f(2,3, "%") returns 2
# f(2,3, "**") returns 8
# f(2,3, "*") returns 6
# f(2,3, "-") returns -1

def f(number1, number2, operator):
    if operator == "+":
        result = number1+number2
    elif operator =="-":
        result = number1-number2
    elif operator == "*":
        result=number1*number2
    elif operator == "%":
        result = number1%number2
    elif operator == "**":
        result = number1**number2
    return print(result)

f(2,3, "*")