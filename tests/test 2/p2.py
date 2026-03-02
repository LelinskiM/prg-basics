def f(number):
    x1=0
    x2=1
    x3=0
    while x1< number:
        x3=x1+x2
        x1=x2
        x2=x3
    if x1 == number:
        return True
    else:
        return False
