x=0
while x<=30:
    if x%3==0 and x%5==0:
        print("BiNGO")
    elif x%3==0:
        print("THREE")
    elif x%5==0:
        print("FIVE")

    else:
        print(x)
    x+=1
