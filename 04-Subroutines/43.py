# 44.	A valid password should consist of at least six different characters. Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:
# f("ax15") returns False
# f("book123") returns False
# f("A2water3") returns True
# f("qwerty") returns True
# f("") returns False

def f(password):
    password_check = password.split()
    symbols = []
    freq_count = 1
    for i in password_check:
        symbols.append(i)
        if i in symbols:
            freq_count += 1
    print(password_check)
    if len(password)>=6:
        return True
    else:
        return False


f("hhhh")