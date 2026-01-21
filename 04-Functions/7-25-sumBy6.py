def f(x,y):
    total = 0
    for i in range(x,y+1):
        if i % 6 == 0 and i % 4 !=0:
            total += i
    return total

print(f(1,20)) # returns 24
print(f(10,30)) # returns 48