x= [15, 8, 31, 47, 2, 19]
i=0
while i < len(x) // 2:
    temp= x[i]
    x[i]= x[len(x) - 1 - i]
    x[len(x) - 1 - i]= temp
    i += 1
print(x)