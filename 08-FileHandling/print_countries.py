###
# Reads from file, line by line
#
x=1
with open('countries.txt', 'r') as file:
    for line in file:
        print(x,".",line, end="")
        x+=1