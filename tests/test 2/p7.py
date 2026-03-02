def f(array2D):
    total=0
    for key,value in array2D:
        print(key,":",value)
        total +=key
        total -=value
    return total