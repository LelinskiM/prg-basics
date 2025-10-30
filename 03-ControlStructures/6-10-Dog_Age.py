Dog_age = int(input("Enter your dog's age in human years: "))
dog_Year = 0
while Dog_age >= 1:
    if Dog_age <=2:
        dog_Year += 10.5
        Dog_age -= 1
    else:
        dog_Year += 4
        Dog_age -= 1
print("Your dog's age in dog years is:", dog_Year)