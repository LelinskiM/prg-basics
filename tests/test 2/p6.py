def f(addr):

    a=("abcdefghigklmnopqrstuvwsyz")
    A=("ABCDEFGHIJKLMNOPQRSTUVWSYZ")
    num=("1234567890")
    c1=0
    c2=0
    a3=0
    n1=0
    n2=0
    r=0


    for i in range(len(addr)):
        c3=0
        for j in addr:
            
            if i == 0 or i == 1:
                
                if c3>1:
                    return False
                for a1 in a:
                    if a1==j:
                        c1+=1
                for a2 in A:
                    if a2==j:
                        c2+=1
                for a3 in num:
                    if a3==j and i==0:
                        c3 +=1

            if i>1 and i<=5:
                
                for n1 in a:
                    if n1==j:
                        return False
                for n2 in A:
                    if n2==j:
                        return False
    r=c1+c2
    if r>2:
        return False
    else:
        return True

 
