def f(n):

    dig = str(n)
    total = 0

    for i in "1234567890":
        count = 0
        for j in dig:
            if i == j:
                count += 1
        if count > 1:
            total += (int(i) * count)
    return total

print(f(1027)) #returns 0
print(f(230335)) #returns 9
print(f(513553007)) #returns 21
