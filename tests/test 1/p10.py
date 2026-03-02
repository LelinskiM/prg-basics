def f(time1, time2):
    t1=0
    t2 =0
    for i in time1:
        if i == "p":
            t1+=1
        elif i =="a":
            t1-=1

    for j in time2:
        if j == "p":
            t2+=1
        elif i =="a":
            t2-=1

    if t1<t2:
        return time1
    elif t1>t2:
        return time2
    else:
        if time1>time2:
            return time2
        else:
            return time1
