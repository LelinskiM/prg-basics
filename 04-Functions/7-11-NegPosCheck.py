def numbers(n1,n2,n3):
    neg_count = 0
    pos_count = 0
    for num in (n1, n2, n3):
        if num < 0 and num % 2 == 0:
            neg_count += 1
        elif num > 0 and num % 2 != 0:
            pos_count += 1
    if neg_count == 0:
        return(False)
    else:
        return (True)

print(numbers(-2,3,4))
print(numbers(11,6,-4))
print(numbers(6,9,2))