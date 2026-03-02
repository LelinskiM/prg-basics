def f(student1, student2):

    s1=0
    s2=0
    x=0
    for x in student1:
        if x == "1" or x == "2" or x == ",":
            s1 += 0
        else:
            s1 += 1
    for y in student2:
        if y == "1" or y == "2" or y == ",":
            s2 += 0
        else:
            s2 += 1



    if s1 > s2:
        return 1
    elif s1 < s2:
        return 2
    else: return 0
