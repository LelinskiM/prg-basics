def f(n):
    if n==1:
        return "*"*n
    elif n==0:
        return ("")
    else:
        return ("*/" * (n-1) + "*")

print(f(5))
print(f(3))
print(f(0))
print(f(1))