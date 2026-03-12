def f(vname):
    alf = "abcdefghijklmnopqrstuvwxyz_"
    ALF = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "12345678910"
    count1=0
    count2=0

    if len(vname)>6:
        return False
    
    for i in vname:
        if count1 < 1:
            if i in alf or i in ALF:
                count2 += 0
            else:
                count2+=1
        elif count1 >=1:
            if i in alf or i in ALF or i in nums:
                count2 += 0
            else:
                count2 +=1

    if count2 > 0:
        return False
    else:
        return True