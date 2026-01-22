def f(n):
    total = 0
    count = 0
    for i in n:
        if count <= 2:
            total += int(i)
            count += 1
        elif count == 3:
            if total % 7 == int(i):
                return True
    return False

print(f("1082")) #returns True
print(f("2035")) #returns True
print(f("1114")) #returns False
print(f("7071")) #returns False