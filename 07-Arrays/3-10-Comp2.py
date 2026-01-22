def f(a1, a2):
    for i in range(len(a1)):
        if a1[i] not in a2:
            print (a1[i])

f([4,36,12,28,9,44,5], [5,1,36])