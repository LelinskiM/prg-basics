x=[15, 8, 31, 47, 2, 19]
mean = 0
mean1 = 0
y=0
for i in range(len(x)):
    mean += x[i]
mean /= len(x) 

while y < len(x):
    mean1 += x[y]
    y += 1
mean1 /= len(x)
print("List:", x)
print("Mean:", mean)
print("Mean using while loop:", mean1)