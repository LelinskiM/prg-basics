Time_parcked = int(input("Enter the number of hours parked: "))
fee = 0
if Time_parcked <= 2:
    fee += 5
elif Time_parcked <= 6:
    fee += 15
elif Time_parcked > 6:
    fee += 25

print("The parking fee is: ", fee,"zł")