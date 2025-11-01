for i in range(6,-1,-3):
    for j in range(1,4):
        print(f'{i+j}',end=' ')
    print()

print("-----")

x = 6
while x >= 0:
    y=1
    while y <= 3:
        print(f'{x+y}', end=' ')
        y += 1
    print()
    x -= 3