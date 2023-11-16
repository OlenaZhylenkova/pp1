import count

text = input("Enter the text: ")
letter = input("Enter the letter: ")
e = "e"

count.count_let(text, letter)
print(f"the number of letter {letter} is {count.count_let(text, letter)}")

count.count_e(text)
print(f"the number of letter 'e' is {count.count_e(text)}")


# def count_letter(text):
#     count = 0
#     for i in text:
#         if i == e:
#             count+=1
#     return count

# def count_e(text, letter):
#     count_e = 0
#     for i in text:
#         if i == letter:
#             count_e+=1
#     return count_e
    
