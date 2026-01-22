###
# Reads from file, line by line
#
x=1
with open('countries.txt', 'r') as file:
    for i in file:
        print(x,".",i, end='')
        x+=1