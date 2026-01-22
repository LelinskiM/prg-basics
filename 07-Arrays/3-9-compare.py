def f(a1, a2):
    if len(a1) != len(a2):
        return False
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return False
    return True

print(f(["water","book","sky"], ["water","book","sky"]))
print(f([True,False], [True,False,True]))
print(f([5,3,1], [5,3,1]))
print(f([3,2,1], [3,2]))