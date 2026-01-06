def numbers(x,even):
    count = 0
    if even == True:
        for char in x:
            if int(char) % 2 == 0:
                count += int(char)
    else:
        for char in x:
            if int(char) % 2 != 0:
                count += int(char)
    return count

print(numbers("3124",True))
print(numbers("3124",False))
print(numbers("20576",False))
print(numbers("20576",True))
print(numbers("13115",True))
