def f(n):
    print(n)
    print(len(n))
    print(n[0])
    print(n[1])
    print(n[-1])
    print(n[len(n)-1])
    print(n[0]+n[-1])
    print(n[len(n)//2])
    for i in range(len(n)):
        print(n[i], end=" ")

f([2,3,7,5,4])