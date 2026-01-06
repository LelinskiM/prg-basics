def coin(n):
    count=0
    while n>=5:
        n-=5
        count+=1
    while n>=2:
        n-=2
        count+=1
    while n>=1:
        n-=1
        count+=1
    return count

print(coin(23))
print(coin(8))
print(coin(2))
print(coin(0))