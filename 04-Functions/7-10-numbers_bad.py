def numbers(x,y):
    count = 0
    while x <= y:
        #z=x *-1
        if (x*-1)%2 == 0 and x<0:
            count += 1
            x +=1
        else:
            x +=1
    return count

print(numbers(-7,8))
print(numbers(-1,11))