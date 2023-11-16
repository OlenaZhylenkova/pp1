# 39.	A sentence is an ordered group of words separated by spaces (spaces). Define a function f(sentence) that returns a sentence with spaces removed. Sample result:
# f("integrated development environment") returns "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing computer programs") returns "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms" 

def f(text):
    text_new = text.replace(" ", "")
    print(text_new)
    return text_new

f("Gello lgiog fjhsf")