def f(n):
    n1=0
    n2=1
    n3=0

    for i in range(n-2):
        n1 = n1+n2
        n3=n1
        n1=n2
        n2=n3
    return n2

print(f(7))
print(f(5))
print(f(9))