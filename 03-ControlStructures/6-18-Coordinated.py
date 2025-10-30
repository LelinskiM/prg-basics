x=int(input("Enter a coordinate (x): "))
y=int(input("Enter a coordinate (y): "))

if x>0 and y>0:
    print("The coordinate is in the First Quadrant.")
elif x<0 and y>0:
    print("The coordinate is in the Second Quadrant.")  
elif x<0 and y<0:
    print("The coordinate is in the Third Quadrant.")
elif x>0 and y<0:
    print("The coordinate is in the Fourth Quadrant.")