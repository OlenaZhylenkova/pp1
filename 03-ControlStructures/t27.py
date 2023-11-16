facebook = True
twitter = False
instagram = True

if facebook and instagram:
    print("Good")
elif facebook and twitter:
    print("Good")
elif twitter and instagram:
    print("Good")
else:
    print("False")