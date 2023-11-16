# 47.	Define a function f(text) that returns the given text with all characters separated by "-" (minus sign). Example:
# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""


def f(text):
    text_list = []
    for char in text:
        text_list.append(char)
    return "-".join(text_list)

print(f("university"))