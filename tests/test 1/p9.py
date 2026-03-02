def f(size):
    scount=0
    mcount=0
    lcount=0
    for i in size:
        if i =="S":
            scount+=1
        elif i == "M":
            mcount += 1
        elif i == "L":
            lcount += 1
    if scount < mcount and scount < lcount:
        return "S"
    elif mcount < scount and mcount < lcount:
        return "M"
    else:
        return "L"
