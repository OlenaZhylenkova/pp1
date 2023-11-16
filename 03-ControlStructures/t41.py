pin = "0805"

entered_pin = input("Enter your PIN code: ")

attempt = 0
if pin == entered_pin:
     print("valid")
else:
    for attempt in range(0,2):
        if pin == entered_pin:
                print("valid")
        elif attempt != 3:
            print("invalid pin")
            attempt+=1
            entered_pin = input("Enter your PIN code: ")
    print("invalid")
    print("card blocked")