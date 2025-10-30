Car_Speed = int(input("Enter the speed of the car in km/h: "))
Speed_Limit_Max = 140
Speed_Limit_Min = 40

if Car_Speed > Speed_Limit_Max:
    print("Warning! You are exceeding the maximum speed limit!")
elif Car_Speed < Speed_Limit_Min:
    print("You are below the minimum speed limit!")
else:
    print("You are within the speed limits.")
