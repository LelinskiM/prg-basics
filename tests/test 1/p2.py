def f(things_to_wash, extra_rinse,extra_spin):
    total=0
    if things_to_wash == "J":
        total += 40
    elif things_to_wash == "U":
        total += 70
    elif things_to_wash == "S":
        total += 20
    if extra_rinse == True:
        total += 15
    if extra_spin == True:
        total += 9
    return total