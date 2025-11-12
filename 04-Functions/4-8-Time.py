

def Time_String(hours, minutes, time_Format):
    if time_Format == 12:
        if hours>=12:
            return (print(f"{hours-12}:{Time_correction_M(minutes)}Pm"))
        else:
            return (print(f"{Time_correction_H(hours)}:{Time_correction_M(minutes)}am"))
    else:
        return((print(f"{ Time_correction_H(hours)}:{Time_correction_M(minutes)}")))
    
def Time_correction_H(hours):
    if hours < 0 or hours > 23:
        return False
    else:
        if hours < 10:
            hours = "0" + str(hours)
    return hours
def Time_correction_M(minutes):
    if minutes < 0 or minutes > 59:
        return False
    else:
        if minutes < 10:
            minutes = "0" + str(minutes)
    return (minutes)

hours = int(input("enter the hour: "))
minutes = int(input("Enter the minutes: "))
time_Format = int(input("Enter the time format: "))
print(Time_String(hours, minutes, time_Format))