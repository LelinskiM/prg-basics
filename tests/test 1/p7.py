def f(a,b):
    c=0
    x1=0
    x2=1
    x3=0
    sum = 0
    while x1 < b:
        x3=x1+x2
        x1=x2
        x2=x3
        if x1>=a:
            sum +=x1
    return sum

print(f(30,90))