def f(n):
    RepeteAmount=0
    largestNum=0
    LNRC=0
    for i in range(1, len(n)):
        if n[i]==n[i-1]:
            RepeteAmount+=1
            if RepeteAmount>LNRC:
                largestNum=n[i]
                LNRC=RepeteAmount
        else:
            RepeteAmount=0
    return largestNum

print(f("5233165554211")) #returns 5
print(f("2133")) #returns 3