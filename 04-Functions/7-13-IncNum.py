def f(n):
    x = ""
    for i in range(n):
        x = str(x) + str(i + 1)
    return x

print(f(5))
print(f(3))
print(f(11))