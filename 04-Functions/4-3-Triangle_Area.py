###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
def triangle_area(a,b,c):
    s=(a+b+c)/2 
    A= math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A

print(f'The area of ​​a triangle with sides a={a}, b={b}, c={c} is: ',triangle_area(a,b,c))
