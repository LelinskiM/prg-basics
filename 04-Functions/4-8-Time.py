

def Time_String(hours, minutes, time_Format):
    if time_Format == 12:
        if hours>=12:
            return (print(f"{hours-12}:{minutes}Pm"))
        else:
            return (print(f"{hours}:{minutes}am"))
    else:
        return((print(f"{hours}:{minutes}")))

    return 

hours = int(input("enter the hour: "))
minutes = int(input("Enter the minutes: "))
time_Format = int(input("Enter the time format: "))
print(Time_String)