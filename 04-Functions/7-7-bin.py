def bin(n):
    for char in n:
        if char not in "01":
            return False
    return True

print(bin("1010101"))  # True
print(bin("1020101"))  # False