def count_e(text):
    count_e = 0
    for i in text:
        if i == "e":
            count_e+=1
    return count_e

def count_let(text, letter):
    count_let = 0
    for i in text:
        if i == letter:
            count_let+=1
    return count_let