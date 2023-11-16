def mask_card(card_number):
    count = 0
    masked_card= []
    for i in card_number:
        count+=1
        if count>2 and count<13:
            new_i = i.replace(i, "*")
            masked_card.append(new_i)
        else:
            masked_card.append(i)
    return print("".join(masked_card))


    
