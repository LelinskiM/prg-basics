def f(dates):
    num="1234567890"
    arry=[]
    i=0
    while i <= len(dates):
        if dates[i-9] in num and dates[i-8] in num and dates[i-7]=="/" and dates[i-6] in num and dates[i-5] in num and dates[i-4] =="/" and dates[i-3] in num and dates[i-2] in num and dates[i-1] in num and dates[i] in num:
            arry.append(dates[i-9]+dates[i-8]+dates[i-7]+dates[i-6]+dates[i-5]+dates[i-4]+dates[i-3]+dates[i-2]+dates[i-1]+dates[i])
            i+=1
        else:
            i+=1
    return arry

