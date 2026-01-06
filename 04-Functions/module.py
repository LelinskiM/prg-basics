def count_letter(Text, letter):
    count = 0
    for char in Text:
        if char == letter:
            count += 1
    return count

def num_check(x,y,z):
    if z >= x and z <= y:
        return True
    else:
        return False

def hide(card_number):
    print(f"Card number: ",card_number[0:2], end="")
    for char in card_number[2:-4]:
        print("*", end="")
    print(f"{card_number[-4:]}")