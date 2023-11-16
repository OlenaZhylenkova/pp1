# 45.	An expression contains operators for adding and subtracting single-digit numbers. Define a function f(expression) that returns the value of the expression. Sample result:
# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6

def calculate_expression(expression):
    # Initialize variables to store the result and the current number
    result = 0
    current_number = 0
    # Initialize a variable to keep track of the current operator (+ or -)
    current_operator = '+'

    # Iterate through each character in the expression
    for char in expression:
        if char.isdigit():
            # If the character is a digit, convert it to an integer and update the current number
            current_number = current_number * 10 + int(char)
        elif char in ('+', '-'):
            # If the character is an operator, update the result based on the current operator and number
            if current_operator == '+':
                result += current_number
            elif current_operator == '-':
                result -= current_number
            # Update the current operator and reset the current number
            current_operator = char
            current_number = 0

    # After the loop, handle the last number in the expression
    if current_operator == '+':
        result += current_number
    elif current_operator == '-':
        result -= current_number

    return result

# Sample results
print(calculate_expression("2+3"))      # Output: 5
print(calculate_expression("3+8+1"))    # Output: 12
print(calculate_expression("2+3-4+5-0"))# Output: 6
