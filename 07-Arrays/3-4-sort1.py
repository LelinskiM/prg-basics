x=[-15, 8, -31, 47, -2, 19]

for i in range(len(x)-1):
    for j in range(len(x)-1-i):
        if x[j]>x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
print("max:", x[-1])
print("min:", x[0])