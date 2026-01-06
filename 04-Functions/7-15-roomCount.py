def f(detector):
    count = 0
    max = 3

    for sym in detector:
        if sym == "+":
            count += 1
        elif sym == "-":
            count -= 1  
        if count>= max:
            return True
            break
        else:
            continue
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))