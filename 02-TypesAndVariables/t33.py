password = input("Enter password: ")

len = len(password)
if len < 8 :
    print("Password is valid: False")
else:
    print("Password is valid: True")